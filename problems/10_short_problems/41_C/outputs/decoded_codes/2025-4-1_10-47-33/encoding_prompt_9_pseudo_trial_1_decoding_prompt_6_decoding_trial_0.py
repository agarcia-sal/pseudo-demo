# Step 1: Receive Input
input_string = input().strip()  # Read a line of input and remove surrounding whitespace

# Step 2: Replace Word Aliases
input_string = input_string.replace("dot", ".")  # Replace "dot" with "."
input_string = input_string.replace("at", "@")    # Replace "at" with "@"

# Step 3: Adjust Beginning of String
if input_string.startswith("."):  # Check if the first character is "."
    input_string = "dot" + input_string  # Prepend "dot" to the string

# Step 4: Initialize Counters
at_counter = 0  # to track occurrences of "@"
modified_string_list = []  # to store characters of the modified string

# Step 5: Handle Special Cases for Starting Character
if input_string.startswith("@"):  # Check if the first character is "@"
    input_string = "at" + input_string[1:]  # Replace first character with "at"

# Step 6: Iterate through Each Character
for char in input_string:
    if char == "@":
        if at_counter > 0:  # If this is not the first occurrence of "@"
            modified_string_list.append("at")  # Append "at" instead of "@" 
            at_counter = 1  # Update counter
        else:
            modified_string_list.append(char)  # Append "@" the first time
            at_counter = 1  # Update counter
    else:
        modified_string_list.append(char)  # Append non-"@" characters as they are

# Step 7: Combine List into String
modified_string = ''.join(modified_string_list)  # Join the list back into a single string

# Step 8: Adjust End of String
if modified_string.endswith("."):  # Check if the last character is "."
    modified_string = modified_string[:-1] + "dot"  # Replace it with "dot"

# Step 9: Output Modified String
print(modified_string)  # Print the final modified string
