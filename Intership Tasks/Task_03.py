# password_generator.py Task_03

import random
import string

def generate_password(length):
    # Define possible characters (uppercase, lowercase, digits, symbols)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("----- Password Generator -----")
    
    try:
        length = int(input("Enter the desired password length: "))
        
        if length < 4:
            print("Password length should be at least 4 characters for security.")
            return
        
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
    
    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
