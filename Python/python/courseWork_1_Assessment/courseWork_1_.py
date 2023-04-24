
def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")


def enter_message():
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
        if mode == "e" or mode == "d":
            break
        else:
            print("Invalid Mode.")

    data = input(
        "Would you like to read from a file (f) or the console (c)? ")

    if data == "c" and mode == "e":
        message = input("What message would you like to encrypt: ")
    elif data == "c" and mode == "d":
        message = input("What message would you like to decrypt: ")
    # If the datais a file, get the message from the file
    elif data == "f":
        while True:
            filename = input("Enter a filename: ")
            try:
                with open(filename, 'r') as f:
                    message = f.read()
                break
            except FileNotFoundError:
                print("Invalid Filename")

    # If the data is invalid, ask again
    else:
        print("Invalid input")
        return enter_message()
    return (mode, message)


# Define the encrypt function to encrypt the message with a given shift
def encrypt(message, shift):
    # Initialize an empty string for the result
    result = ""
    # Iterate through each character in the message
    for char in message:
        # If the character is a letter, encrypt it
        if char.isalpha():
            # Get the ASCII code for the character
            char_code = ord(char)
            # If the character is uppercase, encrypt it using uppercase ASCII codes
            if char.isupper():
                char_code = ((char_code - 65 + shift) % 26) + 65
            # If the character is lowercase, encrypt it using lowercase ASCII codes
            else:
                char_code = ((char_code - 97 + shift) % 26) + 97
            # Convert the ASCII code back to a character and add it to the result string
            char = chr(char_code)
        result += char
    # Return the encrypted message
    return result


# Define the decrypt function to decrypt the message with a given shift
def decrypt(message, shift):
    # Decrypt the message using the encrypt function with a negative shift
    return encrypt(message, -shift)


# Define the main function to run the program
def main():
    # Print the welcome message
    welcome()
    # Loop through the program until the user chooses to quit
    while True:
        # Get the message and mode from the user
        mode, message = enter_message()
        # Get the shift from the user
        while True:
            try:
                shift = int(input("What is the shift number: "))
                break
            except ValueError:
                print("Invalid Shift")

        # Encrypt or decrypt the message based on the user's mode
        if mode == "e":
            result = encrypt(message, shift)
        elif mode == "d":
            result = decrypt(message, shift)
        else:
            print("Invalid Input")
            continue
        # Print the result
        print(result)

        # Ask the user if they want to encrypt or decrypt another message
        while True:
            answer = input(
                "Would you like to encrypt or decrypt another message? (y/n): ")
            if answer == "y":
                break
            elif answer == "n":
                print("Thanks for using the program, goodbye!")
                return
            else:
                print("Invalid Input")
        print()


main()
