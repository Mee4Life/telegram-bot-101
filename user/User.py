class User:
    '''
    User Class: 
        Object Variables:   
            id: User ID 
            fname: User First Name
            level: User in App Level
            msgs: Messages Array
    '''
    def __init__ (user):
        user.id = None
        user.fname = None
        user.level = 'register'
        user.msgs = []