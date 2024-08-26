import random
import string

def generate_password(length=12):
    # Define the character sets
    letters = string.ascii_letters  # a-zA-Z
    digits = string.digits          # 0-9
    special_chars = string.punctuation  # Special characters like !, @, #, etc.

    # Combine all the characters
    all_chars = letters + digits + special_chars

    # Randomly select characters from the combined set
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

# Generate a random password of desired length
password_length = 12
print(f"Generated password: {generate_password(password_length)}")
