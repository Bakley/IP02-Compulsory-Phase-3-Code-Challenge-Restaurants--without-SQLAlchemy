class User:
    
    def __init__(self, name, email) -> None:
        self.id = 0
        self.name = name
        self.email = email
        self.age = 0
        
        
user1 = User("Mansa Msa", 'mansa@msa.org')
print(user1)