class User:

  def __init__(self, user_id, username):
    self.id = user_id
    self.username = username
    self.followers = 0

user1 = User("001", "jang")
user2 = User("002", "jack")

print(user1.username)
print(user2.id)
print(user2.followers)

