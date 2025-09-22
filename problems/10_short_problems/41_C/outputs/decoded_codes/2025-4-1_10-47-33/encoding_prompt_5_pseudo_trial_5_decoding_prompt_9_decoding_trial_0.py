# This program formats a string to resemble an email by replacing
# certain words with symbols and adjusting its structure.

# Read input from the standard input and remove trailing spaces
input_string = input().strip()
original_string = input_string

# Replace occurrences in the string
original_string = original_string.replace("dot", ".")
original_string = original_string.replace("at", "@")

# Check if the first character is a dot
if original_string.startswith("."):
    original_string = "dot" + original_string

# Initialize variables to manage email formatting
previous_char = 0    # To track the last occurrence of '@'
formatted_characters = []  # List to store formatted characters

# Check if the string starts with an '@'
if original_string.startswith("@"):
    formatted_characters.append("at")

# Iterate through each character in the modified string
for character in original_string:
    if character == "@":
        if previous_char > 0:
            formatted_characters.append("at")
        else:
            formatted_characters.append("@")
        previous_char = 1  # Update to indicate '@' was found
    else:
        formatted_characters.append(character)
        previous_char = 0  # Reset if not '@'

# Join the formatted characters into a single string
final_string = ''.join(formatted_characters)

# Check if the last character of the formatted string is a dot
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Print the final formatted string
print(final_string)
