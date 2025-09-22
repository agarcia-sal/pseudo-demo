# Step 1: Read input from the user
user_input = input().strip()  # Remove leading and trailing whitespace

# Step 2: Replace substrings
user_input = user_input.replace("dot", ".")
user_input = user_input.replace("at", "@")

# Step 3: Adjust starting character
if user_input.startswith("."):
    user_input = "dot" + user_input

# Step 4: Initialize variables
at_counter = 0  # To count occurrences of '@'
converted_characters = []  # List to hold processed characters

# Step 5: Handle @ character
if user_input.startswith("@"):
    user_input = "at" + user_input[1:]  # Replace "@" at the start with "at"

# Step 6: Process each character
for current_char in user_input:
    if current_char == "@":
        if at_counter > 0:  # If "@" has been seen before
            converted_characters.append("at")
            at_counter = 1
        else:
            converted_characters.append("@")
            at_counter = 1
    else:
        converted_characters.append(current_char)

# Step 7: Combine converted characters
result = ''.join(converted_characters)

# Step 8: Final adjustments
if result.endswith("."):
    result = result[:-1] + "dot"  # Replace last '.' with 'dot'

# Step 9: Output the result
print(result)
