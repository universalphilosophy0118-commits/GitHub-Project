import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Please enter a number.")
    exit()

if length <= 0:
    print("Password length must be greater than 0.")
    exit()

if length > 100:
    print("Password length must be 100 or less.")
    exit()
password = ""

for i in range(length):
    password += random.choice(characters)

print("Your password:", password)