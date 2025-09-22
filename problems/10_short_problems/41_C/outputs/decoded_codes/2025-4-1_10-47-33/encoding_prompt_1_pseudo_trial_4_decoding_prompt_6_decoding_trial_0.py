# Start of the program

# Step 1: Read input string and remove leading/trailing whitespace
input_string = input().strip()

# Step 2: Replace "dot" with "." in the input string
modified_string = input_string.replace("dot", ".")

# Step 3: Replace "at" with "@" in the updated string
modified_string = modified_string.replace("at", "@")

# Step 4: Prepend "dot" if the first character is "."
if modified_string and modified_string[0] == ".":
    modified_string = "dot" + modified_string[1:]

# Step 5: Initialize the counter for consecutive "@"
consecutive_at_counter = 0

# Step 6: Initialize an empty list to hold processed characters
processed_characters = []

# Step 7: Initialize a variable (unused in logic, kept for structure)
unused_variable = 0

# Step 8: Prepend "at" if the first character is "@"
if modified_string and modified_string[0] == "@":
    modified_string = "at" + modified_string[1:]

# Step 9: Process each character in the modified string
for character in modified_string:
    if character == "@":
        if consecutive_at_counter > 0:  # If "@" has been seen already
            processed_characters.append("at")
            consecutive_at_counter = 1
        else:
            processed_characters.append(character)
            consecutive_at_counter = 1
    else:
        processed_characters.append(character)
        consecutive_at_counter = 0  # Reset counter for other characters

# Step 10: Join all characters into a single string
final_string = ''.join(processed_characters)

# Step 11: Replace the last character with "dot" if it is "."
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"

# Step 12: Print the final processed string
print(final_string)

# End of the program
