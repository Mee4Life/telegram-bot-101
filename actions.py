from message.message import Message

def registerUser(update, context):
    '''
    **Action = register**
    1. Fetch User from the DB
    2. Save received User Msg 
    3. Send User Message 
    4. Save Bot sended Message
    5. Save User to DB
    '''
    # Fetch User from DB
    user = context.user_data['user']
    # Save received User Msg 
    saveUserMsg(update, context, source='update')
    # Send User Message 
    msg = context.bot.send_message(
        chat_id=update.effective_chat.id, text='*Me 4 Life   \|   Register*', parse_mode='MarkdownV2')
    # Save Bot sended Message
    saveUserMsg(update, context, source='context', contextMSG=msg)
    # Save User to DB
    context.user_data['user'] = user

def DeleteUserChat(update, context):
    '''
    **Action = deleteChat**
    1. Fetch User from the DB
    2. Save received User Msg 
    3. Extract Chat ID from the Update.
    4. Loop throw User MSGs and Delete
    5. Clean User Messages Array in the DB
    6. Save User to DB
    '''
    # 1. Fetch User from the DB
    user = context.user_data['user']
    # 2. Save received User Msg 
    saveUserMsg(update, context, source='update')
    # 3. Extract Chat ID from the Update.
    chat_id = update.message.chat.id
    # 4. Loop throw User MSGs and Delete
    for msg in user.msgs:
        context.bot.deleteMessage(chat_id= chat_id, message_id=msg.id)
    # 5. Clean User Messages Array in the DB
    user.msgs = []
    # 6. Save User to DB
    context.user_data['user'] = user

def saveUserMsg(update, context, source, contextMSG=None):
    '''
    ** -> ( Received / Sended ) Msgs ( from / to ) User **
    1. Check Msg Source if Received Or Sended
    2. Extract Msg Data 
    3. Save in User MSGs in DB
    4. -> Msg OBJ
    '''
    # 1. Check Msg Source Received
    if source == 'update':
        # 2. Extract Msg Data 
        user = context.user_data['user']
        msg = Message(update, sourceType=source)
        # 3. Save in User MSGs in DB
        user.msgs.append(msg)
        # 4. -> Msg OBJ
        return msg
    # 1. Check Msg Source Sended
    if source == 'context':
        # 2. Extract Msg Data 
        user = context.user_data['user']
        msg = Message(contextMSG, sourceType=source)
        # 3. Save in User MSGs in DB
        user.msgs.append(msg)
        # 4. -> Msg OBJ
        return msg

dispatcher = {
    'register': registerUser,
    'deleteChat': DeleteUserChat
}