import menu 

#==============
#=== Class ====
#==============

class user():
    id = 0
    def __init__(self, username, password):
        user.id +=1
        self.user_id = user.id
        self.username = username
        self.password = password
        
    def changePassword(self, newPassword):
        self.password = newPassword
        print(f"The user: {self.username} with and id equals to: {self.user_id} has succesfully change his password")
        
class post():
    id = 0
    def __init__(self, username_id, textField):
        post.id +=1
        self.post_id = post.id
        self.username_id = username_id
        self.textField = textField
        
class comment():
    id = 0
    def __init__(self, username_id ,textField):
        comment.id +=1
        self.comment_id = comment.id
        self.username_id = username_id
        self.textField = textField
        
class message():
    id = 0
    def __init__(self, username_id, post_id, textField):
        message.id +=1
        self.message_id = message.id
        self.username_id = username_id
        self.post_id = post_id
        self.textField = textField
        
#========================
#==== List of tuples ====
#========================

users = []
posts = []
comments = []

#====================
#==== Main While ====
#====================
while True:
    opt = menu.mainMenu()
    if opt == 1: #Manage users
        opt2 = menu.manageUsers()
        if opt2 == 1: #Create new user
            users.append(menu.createUser(user))
        if opt2 == 2:#Get users
            menu.getUsers(users)
    
            

