# Begin the program
# Read input from the user and remove trailing spaces
input_string = input().strip()  # Reading input and removing extra spaces
original_string = input_string  # Store the original input string

# Replace occurrences in the string
original_string = original_string.replace("dot", ".")  # Replacing 'dot' with '.'
original_string = original_string.replace("at", "@")  # Replacing 'at' with '@'

# Check if the first character is a dot
if original_string.startswith("."):
    original_string = "dot" + original_string  # Add 'dot' at the beginning if it starts with '.'

# Initialize variables to manage email formatting
previous_char = 0  # To track if the last occurrence was '@'
formatted_characters = []  # List to hold the final formatted characters

# Check if the string starts with an '@'
if original_string.startswith("@"):
    original_string = "at" + original_string  # Add 'at' at the beginning if it starts with '@'

# Iterate through each character in the modified string
for character in original_string:
    # Check if the character is an '@'
    if character == "@":
        if previous_char > 0:
            formatted_characters.append("at")  # Add 'at' if '@' was previously found
            previous_char = 1  # Update to indicate '@' was found
        else:
            formatted_characters.append("@")  # Add '@'
            previous_char = 1  # Update to indicate '@' was found
    else:
        formatted_characters.append(character)  # Add other characters to the list

# Join the formatted characters into a single string
final_string = ''.join(formatted_characters)  # Combine list into a string

# Check if the last character of the formatted string is a dot
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Remove the last character and add 'dot'

# Print the final formatted string
print(final_string)  # Output the final result
