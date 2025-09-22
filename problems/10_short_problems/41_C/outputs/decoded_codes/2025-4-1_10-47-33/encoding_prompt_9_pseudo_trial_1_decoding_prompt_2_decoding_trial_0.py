# Step 1: Receive Input
input_string = input().strip()

# Step 2: Replace Word Aliases
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Adjust Beginning of String
if input_string.startswith('.'):
    input_string = "dot" + input_string

# Step 4: Initialize Counters
at_counter = 0
modified_chars = []  # To store characters of the modified string

# Step 5: Handle Special Cases for Starting Character
if input_string.startswith('@'):
    modified_chars.append("at")  # Replace the first character with "at"
    at_counter = 1
else:
    at_counter = 0

# Step 6: Iterate through Each Character
for char in input_string:
    if char == "@":
        if at_counter > 0:
            modified_chars.append("at")  # Append "at" if there's already one in the list
        else:
            modified_chars.append("@")  # Append "@" and set the counter
        at_counter = 1
    else:
        modified_chars.append(char)  # Append non-@ characters

# Step 7: Combine List into String
result_string = ''.join(modified_chars)

# Step 8: Adjust End of String
if result_string.endswith('.'):
    result_string = result_string[:-1] + "dot"  # Replace last character with "dot"

# Step 9: Output Modified String
print(result_string)
