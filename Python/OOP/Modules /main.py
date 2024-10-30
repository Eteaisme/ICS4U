class User:
    def __init__(self, id):
        self.id = id
    
    def __lt__(self, other):
        if self.id < other.id:
            return True
        else: 
            return False

user1 = User(18)
user2 = User(25)

if(user1 < user2):
    print("1")