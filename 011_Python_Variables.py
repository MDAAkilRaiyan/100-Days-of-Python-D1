# Using Variables and Finding Length of a String

name = "Md. Aakil Raiyan"

name_length = len(name)

# without Converting to String
print("Hello " + name + "\nYour Name Length is -")
print(name_length)

# With converting to String
print(name + " is a name with a total of " + str(name_length) + " letters")

# String Length Using input function
your_name = input("So, what is your name? ")
print("Your name has got " + str(len(your_name)) + " characters")
