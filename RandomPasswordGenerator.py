import random

string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=/"
inputLength = int(input("Enter the length of password: "))

password = "".join(random.sample(string,inputLength))

print(password)
