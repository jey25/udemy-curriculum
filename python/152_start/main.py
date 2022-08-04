class User:

  def __init__(self, user_id, username):
    self.id = user_id
    self.username = username

user1 = User("001", "jang")
user2 = User("002", "jack")

print(user1.username)
print(user2.id)

