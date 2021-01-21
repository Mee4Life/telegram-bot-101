from telegram.ext import Updater
import logging
import functions
from telegram.ext import CommandHandler, MessageHandler, Filters

# set logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# set token
token = '1555160042:AAEq2GLqKnAifpPmI8GoGVRcVjRdfb3465o'
# create our updater and dispatcher
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

# start handler
start_handler = CommandHandler('start', functions.start)
# input Capture
inputCapture = MessageHandler(
    Filters.text & (~Filters.command), functions.inputCapture)


# link our handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(inputCapture)


# start Bot
updater.start_polling()
