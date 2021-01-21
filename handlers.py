from telegram.ext import CommandHandler, MessageHandler, Filters
import functions

# start handler
start_handler = CommandHandler('start', functions.start)

# on message receive handler
echo_handler = MessageHandler(
    Filters.text & (~Filters.command), functions.echo)
