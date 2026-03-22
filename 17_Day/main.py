# class syntax and pass keyword uses to create empty class and function
class Car:
    pass

santro = Car()
santro.name = "Santro"
santro.model = "2012"
santro.color = "white"

print(f"{santro.name} - {santro.color} - {santro.model}")


class Bike:
    # Constructor
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

splender = Bike("splender","2015","Z Black")
print(f"{splender.name} - {splender.color} - {splender.model}")





# ------------------------------------------------------------------
# ------------------------------------------------------------------


class User:
        def __init__ (self, user_id, username):
                self.user_id = user_id
                self.username = username
                self.followers = 0
                self.following = 0
        def follow(self,user):
                user.followers += 1
                self.following += 1

user1 = User("001","robin")
user2 = User("002","sapna")

user1.follow(user2)
user2.follow(user1)

print(f"user1 \t Followers : {user1.followers}, Following : {user1.following}")
print(f"user2 \t Followers : {user2.followers}, Following : {user2.following}")
