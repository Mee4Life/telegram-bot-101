import main

# start
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

# inputCapture
def inputCapture(update, context):
    message = update.message.text
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=message)
