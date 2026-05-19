import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"

length = int(input("Enter password length: "))

password = ""

for i in range(length):

    random_char = random.choice(characters)

    password += random_char

print("Generated Password:", password)