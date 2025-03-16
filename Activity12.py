import random
import string
def password_generator():
    password = ''
    for i in range(8):
        password += random.choice(string.digits)
    return password
print(password_generator())