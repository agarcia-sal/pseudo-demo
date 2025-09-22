# Step 1: Receive Input
input_string = input().strip()  # Read input and remove leading/trailing whitespace

# Step 2: Replace Specific Strings
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Check Beginning of String
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]

# Step 4: Initialize Variables
at_counter = 0  # Count occurrences of "at"
collected_chars = []  # List to hold collected characters

# Step 5: Handle Starting Character
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# Step 6: Iterate Through Characters
for char in modified_string:
    if char == "@":  # If character is '@'
        if at_counter > 0:
            # Append "at" for subsequent occurrences
            collected_chars.append("at")
        else:
            # Append character '@' for the first occurrence
            collected_chars.append(char)
        at_counter += 1  # Increment the counter for occurrences of "at"
    else:
        # If the character is not '@', append it directly to the list
        collected_chars.append(char)

# Step 7: Combine Collected Characters
final_string = ''.join(collected_chars)  # Join all characters into a single string

# Step 8: Final Adjustment
if final_string.endswith("."):
    # Replace the last character with "dot"
    final_string = final_string[:-1] + "dot"

# Step 9: Output the Result
print(final_string)  # Print the final modified string
