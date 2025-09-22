# Start of the program

# Read input from the user and strip leading/trailing spaces
user_input = input().strip()

# Replace occurrences of substrings
user_input = user_input.replace("dot", ".")
user_input = user_input.replace("at", "@")

# Check if the first character is a dot
if user_input and user_input[0] == ".":
    user_input = "dot" + user_input[1:]  # Prepend 'dot' and remove leading dot

# Initialize variables
counter = 0
char_list = []  # List to hold processed characters

# Check if the first character is an at symbol
if user_input and user_input[0] == "@":
    user_input = "at" + user_input[1:]  # Prepend 'at' and remove leading at

# Process each character in user_input
for current_char in user_input:
    if current_char == "@":
        if counter > 0:
            char_list.append("at")  # Append 'at' if counter > 0
            counter = 1  # Set counter to 1
        else:
            char_list.append("@")  # Append '@'
            counter = 1  # Set counter to 1
    else:
        char_list.append(current_char)  # Append the current character

# Join characters to create final result
final_result = ''.join(char_list)

# Check if the last character is a dot
if final_result and final_result[-1] == ".":
    final_result = final_result[:-1] + "dot"  # Replace last dot with 'dot'

# Output the final result
print(final_result)

# End of the program
