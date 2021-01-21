############ Functions ########
# start
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
# echo
def echo(update, context):
    message = update.message.text
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)
