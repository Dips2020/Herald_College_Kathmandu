# ⬇️Defining the welcome function
def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")


# ⬇️Defining the enter_message function to get input from the user
def enter_message():
    while True:
        # Asking the user for their user_choice to encrypt or decrypt
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode == 'e' or mode == 'd':
            break
        else:
            print("Invalid mode")

# Definig the global variable
    file_source = None
    message = None
    filename = None
    shift = 0

 # Asking the user for the location of the file or console
    while not (message or filename):
        file_source = input(
            "Would you like to read from a file (f) or the console (c)? ").lower()

        if file_source == 'f':
            #
            while not filename:
                filename = input("Enter a filename: ")
                if not is_file(filename):
                    print("Invalid Filename")
                    filename = None
                else:
                    while True:
                        try:
                            shift = int(input("What is the shift number: "))
                            break
                        except:
                            print("Invalid Shift")

        elif file_source == 'c':
            while True:
                try:
                    if mode == "e":
                        message = input(
                            "What message would you like to encrypt: ").upper()
                    elif mode == "d":
                        message = input(
                            "What message would you like to decrypt: ").upper()
                    shift = int(input("What is the shift number: "))
                    break
                except:
                    print("Invalid Shift")
        else:
            print("Invalid source")
    return mode, message, filename, shift


#  This function encrypt the message
def encrypt(message, shift):
    encrypted_text = ''
    for char in message:
        if char.isalpha():
            char = chr((ord(char) - 65 + shift) % 26 + 65)
        encrypted_text += char
    return encrypted_text


def decrypt(message, shift):
    # Decrypting the message using the encrypt function with a negative shift
    return encrypt(message, -shift)


def is_file(filename):
    try:
        open(filename, 'r')
        return True
    except:
        return False

# This funtion writes strings to a file called results.txt, with each item taking up a single line.


def write_messages(messages):
    with open("results.txt", "w") as file:
        for message in messages:
            file.write(message + "\n")


# This funtion process the lines in the file one by one, returning a list of encrypted/decrypted messages.
def process_file(filename, mode, shift):
    messages = []
    with open(filename, "r") as file:
        for line in file:
            message = line.strip().upper()
            if mode == 'e':
                messages.append(encrypt(message, shift))
            else:
                messages.append(decrypt(message, shift))
    return messages


# returns mode message filename shift
def message_or_file():
    mode, message, filename, shift = enter_message()
    return mode, message, filename, shift


# Define the main function to run the program
def main():
    # Calling welcome function
    welcome()
    # Loop through the program until the user chooses to quit
    conditional = True
    while conditional == True:
        mode, message, filename, shift = message_or_file()
        if filename:
            messages = process_file(filename, mode, shift)
            write_messages(messages)

            # Ask the user if they want to encrypt or decrypt another message
            user_choice = input(
                "Would you like to encrypt or decrypt another message? (y/n)").lower()
            if (user_choice) == "n":
                conditional = False
                print("\nThanks for using the program, goodbye!")
        else:
            # Encrypting the message based on the user's user_choice
            if mode == 'e':
                print("Encrypted Message:", encrypt(message, shift))

             # Decrypting the message based on the user's user_choice
            if mode == "d":
                print("Decrypted Message:", decrypt(message, shift))

          # Ask the user if they want to encrypt or decrypt another message
            while True:
                user_user_choice = input(
                    "Would you like to encrypt or decrypt another message? (y/n): ").lower()
                if user_user_choice == "y":
                    break
                elif user_user_choice == "n":
                    print("Thanks for using the program, goodbye!")
                    return
                else:
                    print("Invalid Input")


main()
