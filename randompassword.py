import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    password = ''.join(random.sample(password, len(password)))
    return password

length = 12  
print("Generated Password: password")
