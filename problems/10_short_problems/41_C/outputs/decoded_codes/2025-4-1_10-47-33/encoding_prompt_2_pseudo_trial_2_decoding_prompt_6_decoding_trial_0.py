# Step 1: Receive input and remove leading/trailing whitespace
input_string = input().strip()

# Step 2: Replace specific strings in the input
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Check the beginning of the string for "."
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]

# Step 4: Initialize variables
at_counter = 0  # Counter for occurrences of "at"
collected_characters = []  # List to collect characters
character_index = 0  # Initialize character index (not used further)

# Step 5: Handle starting character if it is "@"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# Step 6: Iterate through characters to process "@" occurrences
for char in modified_string:
    if char == "@":
        if at_counter > 0:  # If "at" has occurred before
            collected_characters.append("at")
        else:  # First occurrence of "@"
            collected_characters.append("@")
        at_counter += 1  # Increment "at" occurrence counter
    else:
        collected_characters.append(char)  # Append other characters

# Step 7: Combine collected characters into a single string
final_string = ''.join(collected_characters)

# Step 8: Final adjustment if last character is "."
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace last character with "dot"

# Step 9: Output the final modified string
print(final_string)
