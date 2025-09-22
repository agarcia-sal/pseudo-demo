# Read a line of input and remove any leading or trailing whitespace
input_string = input().strip()

# Replace occurrences of "dot" with a period (.)
modified_string = input_string.replace("dot", ".")

# Replace occurrences of "at" with an at symbol (@)
modified_string = modified_string.replace("at", "@")

# Check if the first character is a period and prepend "dot" if it is
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]

# Initialize a counter for occurrences of the at symbol and a list for characters
at_counter = 0
character_list = []

# Check if the first character is an at symbol and prepend "at" if it is
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# Iterate over each character in the modified string
for character in modified_string:
    if character == "@":
        if at_counter > 0:
            character_list.append("at")
            at_counter = 1
        else:
            character_list.append(character)
            at_counter = 1
    else:
        character_list.append(character)

# Join the list into a single string
final_string = ''.join(character_list)

# Check if the last character of the final string is a period and replace it with "dot"
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Output the modified string
print(final_string)
