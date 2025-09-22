# Purpose: Transform an email-like string by replacing specific text patterns with appropriate symbols

# Step 1: Receive Input
input_string = input().strip()  # Read the input and strip surrounding whitespace

# Step 2: Replace Text Patterns
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Adjust Leading Character
if modified_string.startswith("."):
    modified_string = "dot" + modified_string  # Prepend 'dot' if the string starts with '.'

# Step 4: Initialize Variables
at_counter = 0  # Counter for occurrences of '@'
result_list = []  # List to store characters

# Step 5: Check for Leading "at"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string  # Prepend 'at' if the string starts with '@'

# Step 6: Iterate Through Each Character
for char in modified_string:
    if char == "@":  # If character is '@'
        if at_counter > 0:  # If we have already encountered an '@'
            result_list.append("at")  # Append 'at' to the list
            at_counter = 1  # Reset counter to 1
        else:
            result_list.append(char)  # Append actual '@' to the list
            at_counter = 1  # Set counter to 1 to track the first occurrence
    else:
        result_list.append(char)  # For all other characters, append to the list

# Step 7: Reconstruct the String
final_string = ''.join(result_list)  # Join the list into a single string

# Step 8: Adjust Trailing Character
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace trailing '.' with 'dot'

# Step 9: Output the Result
print(final_string)  # Print the transformed string
