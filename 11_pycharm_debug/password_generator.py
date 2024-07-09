import random
import string

def generate_password():
    password="".join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=10))
    return password
