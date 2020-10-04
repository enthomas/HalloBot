import telegram
from telegram.ext import messagequeue as mq
from telegram.utils.request import Request

from data import *
from enregistrement import *
from interaction import *
from fonctions import *

# Slightly modify the Bot class to use a MessageQueue in order to avoid
# Telegram's flood limits (30 msg/sec)
class MQBot(telegram.bot.Bot):
    """A subclass of Bot which delegates send method handling to MessageQueue"""
    def __init__(self, *args, is_queued_def=True, mqueue=None, **kwargs):
        super(MQBot, self).__init__(*args, **kwargs)
        self._is_messages_queued_default = is_queued_def
        self._msg_queue = mqueue or mq.MessageQueue()
    def __del__(self):
        try:
            self._msg_queue.stop()
        except:
            pass
    @mq.queuedmessage
    def send_message(self, *args, **kwargs):
        """Wrapped method would accept new `queued` and `isgroup` OPTIONAL arguments"""
        return super(MQBot, self).send_message(*args, **kwargs)


# Limit global throughput to 25 messages per second
q = mq.MessageQueue(all_burst_limit=25, all_time_limit_ms=1000)
# Set connection pool size for bot
request = Request(con_pool_size=8)

def readToken():
    tokfile = open('BOT_TOKEN', 'r')
    token = tokfile.read()[:-1]
    tokfile.close()
    return token

token = readToken()

tgbot = MQBot(token, request=request, mqueue=q)

persistence = telegram.ext.PicklePersistence(filename='bot_data_pickle')

updater = telegram.ext.updater.Updater(bot=tgbot, persistence=persistence, use_context=True)
dispatcher = updater.dispatcher



updater.start_polling()
updater.idle()
