import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    """
    Generate a random password based on given criteria.
    """
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Get user input for password length
        length = int(input("Enter password length: "))
        
        # Get user preferences for character types
        include_letters = input("Include letters (y/n)? ").lower() == 'y'
        include_numbers = input("Include numbers (y/n)? ").lower() == 'y'
        include_symbols = input("Include symbols (y/n)? ").lower() == 'y'
        
        # Generate password
        password = generate_password(length, include_letters, include_numbers, include_symbols)
        
        # Print generated password
        print(f"Generated Password: {password}")
        
    except ValueError:
        print("Error: Please enter a valid number for password length.")
    except KeyboardInterrupt:
        print("\nOperation interrupted.")

if __name__ == "__main__":
    main()
