# Step 1: Input Handling
input_string = input().strip()

# Step 2: Replace Substrings
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Prefix Adjustment
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]

# Step 4: Initialize Variables
counter = 0
outputCharacters = []
length = 0  # This variable is defined but will not be used in the final output

# Step 5: Handle Leading Character
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# Step 6: Iterate Through Each Character
for character in modified_string:
    if character == "@":
        if counter > 0:
            outputCharacters.append("at")
            counter = 1
        else:
            outputCharacters.append("@")
            counter = 1
    else:
        outputCharacters.append(character)

# Step 7: Join Characters
final_output_string = ''.join(outputCharacters)

# Step 8: Trailing Character Adjustment
if final_output_string.endswith("."):
    final_output_string = final_output_string[:-1] + "dot"

# Step 9: Output Result
print(final_output_string)
