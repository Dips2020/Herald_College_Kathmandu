#  Dipesh Bhattarai
#  Student id = 2357842
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

 # This line starts a loop that will continue to run until
 # either the message or filename variable is not empty.
    while not (message or filename):
        file_source = input(
            "Would you like to read from a file (f) or the console (c)? ").lower()

        if file_source == 'f':

            # This line starts a loop that will continue to run until a valid filename is entered.
            while not filename:
                filename = input("Enter a filename: ")
                # This line checks if the entered filename is a valid file.
                if not is_file(filename):
                    # If the filename is not valid,
                    # this line prints an error message and sets the filename variable to None.
                    print("Invalid Filename")
                    filename = None
                else:
                    # This line starts an inner loop that will continue to run until
                    # a valid shift number is entered.
                    while True:
                        try:
                            shift = int(input("What is the shift number: "))
                            break
                        # If the valid shift integer is not entered
                        # then the error message Invalid shift will be printed
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
            # If the user did not enter a valid input for file_source,
            # this line prints an error message.
            print("Invalid source")
    # Once the loop has been exited,
    # this line returns the values of mode, message, filename, and shift.
    return mode, message, filename, shift


# Defining a encrypt function that takes two parameters, message and shift.
def encrypt(message, shift):
    # This line initializes an empty string called encrypted_text,
    # which will be used to store the encrypted message.
    encrypted_text = ''
    # This line starts a loop that iterates over each character
    # in the message parameter.
    for char in message:
        # This line checks if the current character is an alphabetic character.
        if char.isalpha():
            # Calculates the new character by shifting it by the specified shift amount
            # The ord() function converts the character to its ASCII code
            # The ASCII code for 'A' is 65, so we subtract 65 from the ASCII code to get the letter's position in the alphabet (0-25)
            # We add the shift amount to this position, then take the result modulo 26 to ensure it stays within the range 0-25
            # Finally, we add 65 to the result to convert it back to ASCII code for the shifted letter
            char = chr((ord(char) - 65 + shift) % 26 + 65)
         # Adds the current character to the encrypted_text string
        encrypted_text = encrypted_text + char
    # This line returns the final encrypted message.
    return encrypted_text


# Defining a decrypt decrypt that takes two parameters, message and shift.
def decrypt(message, shift):
    # The reason this works is that encrypting the message with a positive shift
    # and then decrypting it with the negative of that shift will
    # undo the encryption and return the original message.
    return encrypt(message, -shift)


# This line defines a function called is_file that takes a filename as a parameter.
def is_file(filename):
    # This function tries to open the file with the given filename for reading.
    try:
        open(filename, 'r')
    # If the file exists and can be opened, it returns True.
        return True
    except:
        # Otherwise, it returns False.
        return False


# This funtion writes strings to a file called results.txt, with each item taking up a single line.
def write_messages(messages):
    with open("results.txt", "w") as file:
        # This code writes each string in the messages list to the file,
        # followed by a newline character.
        # This ensures that each string is on a separate line.
        for message in messages:
            file.write(message + "\n")


# This funtion process the lines in the file one by one, returning a list of encrypted/decrypted messages.
def process_file(filename, mode, shift):
    # Initializing an empty list called messages,
    # then opens the file with the given filename for reading.
    messages = []
    with open(filename, "r") as file:
        for line in file:
            #! .strip() is used to Remove spaces at the beginning and at the end of the string
            message = line.strip().upper()
            if mode == 'e':
                # This code encrypts the message,
                # depending on the value of mode, and appends the result to the messages list.
                messages.append(encrypt(message, shift))
            else:
                # This code decrypts the message,
                # depending on the value of mode, and appends the result to the messages list.
                messages.append(decrypt(message, shift))
    return messages


# This code defines a function called message_or_file.
def message_or_file():
    # This line calls the enter_message() function
    # to get the values of mode, message, filename, and shift.
    mode, message, filename, shift = enter_message()
    # This code returns the values of mode, message, filename, and shift as a tuple.
    return mode, message, filename, shift


# Define the main function to run the program
def main():
    # Calling welcome function
    welcome()
    # Set the conditional variable to True to start the while loop
    conditional = True
    # While loop to keep the program running until the user chooses to quit
    while conditional == True:
        # Call the message_or_file function to get the user's choice of message or file
        mode, message, filename, shift = message_or_file()
        # If the user chose to use a file, process the file and write the results to a new file
        if filename:
            messages = process_file(filename, mode, shift)
            write_messages(messages)

            #! this is for file
            # Ask the user if they want to encrypt or decrypt another message
            user_choice = input(
                "Would you like to encrypt or decrypt another message? (y/n)").lower()
            if (user_choice) == "n":
                conditional = False
                print("Thanks for using the program, goodbye!")

#
        # If the user chose to enter a message directly,
        # encrypt or decrypt the message and ask if they want to encrypt or decrypt another message
        else:
            # Encrypting the message based on the user's user_choice
            if mode == 'e':
                print("Encrypted Message:", encrypt(message, shift))

             # Decrypting the message based on the user's user_choice
            if mode == "d":
                print("Decrypted Message:", decrypt(message, shift))

          # Ask the user if they want to encrypt or decrypt another message
            #! this is for console message
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
