from user.User import User
from actions import dispatcher

# start Command
def start(update, context):
    '''
    **Command /start executed**
    '''
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

# inputCapture
def inputCapture(update, context):
    '''
    **User Input Messages any time**
    1. Set User Info 
    2. Dispatch Action based on the Level
    '''
    # get user info: 
    user = fUser(context, update)

    # Dispatch User Level Action: 
    dispatcher[str(user.level)](update, context)


# extract user : 
def fUser(context, update):
    '''
    **User Input Messages any time**

    Check if the User Already exist in the DB.
    If exist then Fetch it. 
    If not Then create new User OBJ.
    '''
    # check user already in context: 
    if "user" in context.user_data:
        user = context.user_data['user']
        return user

    # create user object if not exist: 
    user = User()
    user.id = update.message.from_user.id
    user.fname = update.message.from_user.first_name
    # put user to context: 
    context.user_data['user'] = user
    return user
