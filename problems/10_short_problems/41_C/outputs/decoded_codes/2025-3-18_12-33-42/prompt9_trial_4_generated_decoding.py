# Receive Input
input_string = input().strip()

# Replace Specific Words
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Ensure Proper Format
if modified_string.startswith("."):
    modified_string = "dot" + modified_string

counter = 0  # Initialize a counter for occurrences of "at"
output_characters = []  # Create an empty list to store processed characters

# Process Each Character
for character in modified_string:
    if character == "@":
        if counter > 0:
            output_characters.append("at")  # Add "at" if we have another instance
            counter = 1  # Set counter to 1 to avoid multiple "at" 
        else:
            output_characters.append("@")
            counter = 1  # Track that an "at" has been added
    else:
        output_characters.append(character)  # Add the character as it is

# Reconstruct the String
final_string = ''.join(output_characters)  # Join the list into a single string
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace the last character with "dot"

# Output the Result
print(final_string)
