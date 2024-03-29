user = ("LUIS AuGUSTo", "PAraDA", 32131231, "luis@gmail.com", 25)

# firstname = user[0].title()
# lastname = user[1].title()
# email = user[2].lower()
# age = user[3]

firstname, lastname, *data = user

print(firstname.title(), lastname.title(), data)
