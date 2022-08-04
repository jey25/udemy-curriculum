class User:

  def __init__(self, user_id, username):
    self.id = user_id
    self.username = username

user1 = User("001", "jang")

print(user1.username)

user2 = User()
user2.id = "002"
user2.username = "jack"