# Step 1: Receive Input
user_input = input().strip()  # Read input and remove surrounding whitespace

# Step 2: Replace Specific Words
user_input = user_input.replace("dot", ".")  # Replace "dot" with "."
user_input = user_input.replace("at", "@")    # Replace "at" with "@"

# Step 3: Handle Leading Dot
if user_input.startswith("."):
    user_input = "dot" + user_input[1:]  # Prepend "dot" before the second character

# Step 4: Initialize Trackers
at_counter = False  # Counter for handling "at" symbols
output_list = []    # List to store characters or symbols

# Step 5: Handle Leading At Symbol
if user_input.startswith("@"):
    user_input = "at" + user_input[1:]  # Prepend "at" before the second character

# Step 6: Process Each Character
for char in user_input:
    if char == "@":
        if at_counter:  # Check if another "at" has been noted
            output_list.append("at")  # Append the word "at"
            at_counter = False  # Reset counter
        else:
            output_list.append(char)  # Append "@" as-is
            at_counter = True  # Set counter
    else:
        output_list.append(char)  # Append other characters as-is

# Step 7: Construct Final Output
final_output = ''.join(output_list)  # Join the output list into a single string
if final_output.endswith("."):
    final_output = final_output[:-1] + "dot"  # Replace last character with "dot"

# Step 8: Display Result
print(final_output)
