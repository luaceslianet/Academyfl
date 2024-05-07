firstName = "Lianet"
lastName = "Luaces"
age = 40
dob = "8/21/1983"

if age > 18:
    message = "Welcome to our site!"
else:
    message = "Come back when you are 18"

#if (type(firstName) != str) or (type(lastName) != str):
if (not isinstance(firstName, str)) or ( not isinstance(lastName, str)):
    print("The first name and last name must be a string")

txt = f"Hello, {firstName} {lastName}. I see that your date of birth is {dob}"
print(txt)
print(message)