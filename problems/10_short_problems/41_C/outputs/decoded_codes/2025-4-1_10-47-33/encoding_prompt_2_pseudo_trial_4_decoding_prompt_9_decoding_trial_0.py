# Read a line of input from the user
input_string = input().strip()

# Replace occurrences of 'dot' with '.' and 'at' with '@'
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Check if the first character is a period
if modified_string.startswith('.'):
    modified_string = "dot" + modified_string

# Initialize a counter for occurrences of '@' and create an empty list for characters
at_counter = 0
character_list = []

# Track the length of the string (not actively used further)
length_of_string = len(modified_string)

# Check if the first character is an '@'
if modified_string.startswith('@'):
    modified_string = "at" + modified_string

# Process each character in the modified string
for character in modified_string:
    if character == "@":
        if at_counter > 0:
            character_list.append("at")  # Append "at" if '@' has been seen before
        else:
            character_list.append(character)  # Append the '@' character
            at_counter += 1  # Update the counter
    else:
        character_list.append(character)  # Append any other character

# Join all characters to form the final modified string
final_string = ''.join(character_list)

# Check if the last character is a period
if final_string.endswith('.'):
    final_string = final_string[:-1] + "dot"  # Replace '.' with 'dot'

# Output the final modified string
print(final_string)
