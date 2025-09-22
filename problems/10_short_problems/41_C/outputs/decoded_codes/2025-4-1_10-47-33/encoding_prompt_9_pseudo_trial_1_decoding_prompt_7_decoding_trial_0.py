# Step 1: Receive Input
input_string = input().strip()  # Read a line of input and remove any surrounding whitespace

# Step 2: Replace Word Aliases
# Replace all instances of "dot" with "." and "at" with "@"
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Adjust Beginning of String
# If the first character is ".", prepend "dot" to the string
if modified_string.startswith("."):
    modified_string = "dot" + modified_string

# Step 4: Initialize Counters
counter = 0  # Counter to track occurrences of "@"
char_list = []  # List to store characters of the modified string

# Step 5: Handle Special Cases for Starting Character
# If the first character is "@", replace it with "at"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# Step 6: Iterate through Each Character
for char in modified_string:
    if char == "@":  # Check if the character is "@"
        if counter > 0:  # If the counter is greater than 0, append "at"
            char_list.append("at")
            counter = 1  # Reset counter
        else:  # Otherwise, append "@"
            char_list.append("@")
            counter = 1  # Set counter to 1
    else:
        char_list.append(char)  # Append non-"@" characters as-is

# Step 7: Combine List into String
final_string = ''.join(char_list)  # Convert list of characters back into a single string

# Step 8: Adjust End of String
# If the last character of the resulting string is ".", replace it with "dot"
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Step 9: Output Modified String
print(final_string)  # Print the final modified string
