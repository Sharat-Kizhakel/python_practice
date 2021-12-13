# zip(iterables)=aggregate elements from 2 or MORE ierables
# it creates a zip object with paired elements stored in TUPLES for each element
usernames = ["Dude", "Bro", "Mister"]
passwords = ["password", "abc123", "guest"]

users = zip(usernames, passwords)
print(type(users))
for i in users:
    print(i)
