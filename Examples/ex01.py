# This is a very basic script 
# to accept a name and city from the user 
# and print a greeting message

name = input("What's your name? ")
city = input("Where are you from? ")

# you may use if-else blocks to conditionally process a code

if name == "":
    # assign a value "friend" only if the name is empty
    name = "friend"

if city == "":
    city = "your city"

print("Hello", name, "how is weather in", city, "?")
