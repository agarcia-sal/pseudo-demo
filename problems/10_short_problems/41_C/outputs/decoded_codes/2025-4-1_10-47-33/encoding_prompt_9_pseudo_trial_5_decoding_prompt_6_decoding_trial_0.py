# Step 1: Receive input from the user
user_input = input().strip()  # Remove any leading or trailing spaces

# Step 2: Replace keywords in the input string
modified_string = user_input.replace("dot", ".").replace("at", "@")

# Step 3: Check for leading symbols
if modified_string.startswith("."):
    modified_string = "dot" + modified_string  # Prepend 'dot' if first character is '.'

# Step 4: Initialize variables
at_counter = 0  # Counter for occurrences of "@"
characters_list = []  # List to hold individual characters
string_length = 0  # Initialize length variable

# Step 5: Check for leading "at"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string  # Prepend 'at' if first character is '@'

# Step 6: Process each character in the modified string
for character in modified_string:
    if character == "@":
        if at_counter > 0:  # Check if another "@" has already been encountered
            characters_list.append("at")  # Append 'at' to the list
            at_counter = 1
        else:
            characters_list.append("@")  # Append '@' to the list
            at_counter = 1
    else:
        characters_list.append(character)  # Append the character directly to the list

# Step 7: Join characters into a single string
transformed_string = ''.join(characters_list)

# Step 8: Check trailing symbols
if transformed_string.endswith("."):
    transformed_string = transformed_string[:-1] + "dot"  # Replace last character '.' with 'dot'

# Step 9: Output the final transformed string
print(transformed_string)
