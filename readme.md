# Me 4 Life &nbsp;&nbsp;|&nbsp;&nbsp; Telegram bot

<br />
<br />

## Need to Know : 
1. Updater : to Fetch Data the from Telegram for you 
2. Dispatcher : to register Handlers from different Types
3. Handlers : to Handler Messages, Commands, Photos, Voices ... 
4. every function that link to handlers need to have 2 params updater, context 
5. we use context in the handler functions to reaction with the user
6. we use updater in the handler functions to get the data Ex. Chat_id User Message extra..

## Getting started: 
### - first thing you need to do is setting logger that will log messages in the console 
```python
# set logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
```
### - and then set you token `token = yourToken` <br />
### - Create Updater 
```python
updater = Updater(token=token, use_context=True)
```
### - Create Dispatcher  
```python
dispatcher = updater.dispatcher
```
### - Create Handlers Functions : 
```python
def echo(update, context):
    # get user Message from the user
    message = update.message.text
    # send message to the user.
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
```
### - Handle User Reactions
```python
#Command Handler
start_handler = CommandHandler('start', func)
#Messages Handler
echo_handler = MessageHandler(Filters.text & (~Filters.command), func)
```
I think the Idea is clear and we don't need any thing else to explain lets going on and create our Bots 

<br />
<br />
<br />