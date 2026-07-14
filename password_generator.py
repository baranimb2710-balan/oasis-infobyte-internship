import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if len(char_pool) == 0 or length < 8:
        return None

    password = ''.join(random.choice(char_pool) 
                       for _ in range(length))
    return password

def main():
    while True:
        length = int(input("Enter password length (min 8): "))
        use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        if password:
            print("Generated password:", password)
        else:
            print("Invalid input. Try again.")

        again = input("Generate another? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
