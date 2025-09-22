# Step 1: Read Input
input_string = input().strip()

# Step 2: Replace Keywords
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Check for Leading Character
if input_string.startswith("."):
    input_string = "dot" + input_string

# Step 4: Initialize Tracking Variables
at_counter = 0
modified_characters = []
char_position = 0  # Not used for direct implementation

# Step 5: Check for Leading "at"
if input_string.startswith("@"):
    input_string = "at" + input_string

# Step 6: Process Each Character in the String
for char in input_string:
    if char == "@":
        if at_counter > 0:  # If we've seen an '@' before
            modified_characters.append("at")
            at_counter = 1  # We update our counter since we just added "at"
        else:
            modified_characters.append("@")
            at_counter = 1
    else:
        modified_characters.append(char)

# Step 7: Combine Characters into Final String
final_string = ''.join(modified_characters)

# Step 8: Check the Last Character
if final_string.endswith('.'):
    final_string = final_string[:-1] + "dot"

# Step 9: Output Result
print(final_string)
