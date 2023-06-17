# Request user to input a string and use .lower() to convert it to lowercase.
# .lower() function is used to make case-insensitive comparisons regardless of how the user enters the input.
input_string = input("Please enter a string (word/ sentence): ").lower()

# While loop begins and continues as long as the condition is true.
while True:
    # Ask user to enter the character that they would like to make disappear and convert it to lowercase.
    character = input("Please enter a character you would like to make disappear ('stop' to exit): ").lower()

    # If character input value is not equal to "stop",
    # for char in character, replace 'char' with "" and store it in the variable 'input_string'.
    if character != "stop":
        for char in character:
            input_string = input_string.replace(char, "")

    # Else, break the loop.
    else:
        break

# Print 'input_string' to display the string with the removed characters.
print(input_string)
