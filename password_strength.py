
password = input("Enter your password: ")

password_length = len(password)

has_number = any(char.isdigit() for char in password)

has_uppercase = any(char.isupper() for char in password)

has_lowercase = any(char.islower() for char in password)

special_characters = "!@#$%^&*"

has_special = any(char in special_characters for char in password)

if not has_number:
    print("Password should contain at least one number.")

if not has_uppercase:
    print("Password should contain at least one uppercase letter.")

if not has_lowercase:
    print("Password should contain at least one lowercase letter.")

if not has_special:
    print("Password should contain at least one special character.")

if password_length < 8:
    print("Weak password")
    exit()

elif password_length < 12:
    print("Medium password")

else:
    if has_number and has_uppercase and has_lowercase and has_special:
        print("Strong password")
        print("Your password is strong!")
    else:
        print("Password is long, but it needs numbers, uppercase, lowercase, and special characters.")