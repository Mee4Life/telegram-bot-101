class Message:
    '''
    Message Class: 
        Create Message Based on Received Msg or Sended. 
    Params: 
        1. message: Message Text
        2. source: Source To extract Msg from / Supported : ( update/context OBJs )
        3. sourceType: Source Name : Supported: update/context
    Object Variables: 
        1. text: Msg Text
        2. id: Msg ID
        3. chatID: Chat x ID
        4. time: Received/Sended At: Time
    '''
    def __init__ (message, source, sourceType):
        # extract msg data from user: 
        if sourceType== 'update':
            message.text = source.message.text
            message.id = source.message.message_id
            message.chatID = source.message.chat.id
            message.time = source.message.date
        # extract msg data from bot: 
        if sourceType == 'context':
            message.text = source.text
            message.id = source.message_id
            message.chatID = source.chat.id
            message.time = source.date
