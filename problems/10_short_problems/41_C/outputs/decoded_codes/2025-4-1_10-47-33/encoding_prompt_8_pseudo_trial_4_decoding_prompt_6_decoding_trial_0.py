# Step 1: Read Input
user_input = input().strip()  # Get input from the user and remove spaces

# Step 2: Replace Specific Words
modified_string = user_input.replace("dot", ".").replace("at", "@")

# Step 3: Handle Leading Period
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]  # Replace leading period with "dot"

# Step 4: Initialize Variables
at_count = 0  # Counter for occurrences of the at-symbol
result_list = []  # List to hold characters of the processed string

# Step 5: Handle Leading At-Symbol
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]  # Replace leading at-symbol with "at"

# Step 6: Process Each Character
for character in modified_string:
    if character == "@":
        if at_count > 0:
            result_list.append("at")  # Append "at" instead of another "@" if previously encountered
            at_count = 1  # Reset counter to indicate we've processed an at-symbol
        else:
            result_list.append(character)  # Append the at-symbol
            at_count = 1  # Set counter to indicate we've encountered an at-symbol
    else:
        result_list.append(character)  # Append the character to the list

# Step 7: Join Characters Together
result_string = ''.join(result_list)  # Combine the list into a single string

# Step 8: Handle Trailing Period
if result_string.endswith("."):
    result_string = result_string[:-1] + "dot"  # Replace trailing period with "dot"

# Step 9: Output the Result
print(result_string)  # Print the final processed string
