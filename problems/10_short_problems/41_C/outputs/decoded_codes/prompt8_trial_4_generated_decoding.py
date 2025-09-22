# Read Input
input_string = input().strip()

# Replace Words with Symbols
input_string = input_string.replace("dot", ".").replace("at", "@")

# Ensure Correct Start
if input_string.startswith("."):
    input_string = "dot" + input_string[1:]

# Initialize Variables
counter = 0
converted_characters = []

# Ensure Correct Start for Email
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]

# Iterate Through Each Character
for character in input_string:
    if character == "@":
        if counter > 0:
            converted_characters.append("at")
            counter = 1
        else:
            converted_characters.append(character)
            counter = 1
    else:
        converted_characters.append(character)

# Join Converted Characters
final_string = ''.join(converted_characters)

# Ensure Correct End
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Output Result
print(final_string)
