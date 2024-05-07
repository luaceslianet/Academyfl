# Prompt the user to enter their first name
firstName = input("Enter your first name: ")
 
# Prompt the user to enter their last name
lastName = input("Enter your last name: ")
 
# Prompt the user to enter their city
city = input("Enter your city: ")
 
# Prompt the user to enter their age
age = int(input("Enter your age: "))  # Convert input to integer
 
# Prompt the user to enter their date of birth
dob = input("Enter your date of birth (MM/DD/YYYY): ")
 
message = "Try again when you are 18"
 
if age > 18:
    message = "Welcome to our site!"
 
# Validate City input
if not city.isalpha():
    message = "Enter a valid city"
 
Welcome = f"Hello, {firstName} {lastName}, I see that your date of birth is {dob}. You live in {city}."
 
print(Welcome)
print(message)
