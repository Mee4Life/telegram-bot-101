from telegram.ext import Updater
import logging
import handlers

# setting up Bot Project

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

# link our handlers
dispatcher.add_handler(handlers.start_handler)
dispatcher.add_handler(handlers.echo_handler)

# start Bot
updater.start_polling()
