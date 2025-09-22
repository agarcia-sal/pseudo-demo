# Step 1: Read a line of input
input_string = input().strip()  # Remove leading and trailing spaces

# Step 2: Replace specific words with symbols
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Check if the first character is a period
if input_string and input_string[0] == '.':
    input_string = "dot " + input_string  # Add "dot" at the beginning

# Step 4: Initialize a counter for occurrences of "@"
at_counter = 0
final_characters = []  # List to store characters for final string
string_length = len(input_string)  # Track the length of the string (not used further)

# Step 5: Check if first character is "@"
if string_length > 0 and input_string[0] == '@':
    input_string = "at " + input_string  # Add "at" at the beginning

# Step 6: Iterate through each character in the modified string
for character in input_string:
    if character == "@":
        if at_counter > 0:  # If "@" was added previously
            final_characters.append("at")
        else:
            final_characters.append(character)
            at_counter += 1  # Update counter to indicate "@" has been added
    else:
        final_characters.append(character)

# Step 7: Join the list into a single string
final_string = ''.join(final_characters)

# Step 8: Check if the last character is a period
if final_string and final_string[-1] == '.':
    final_string = final_string[:-1] + "dot"  # Replace period with "dot"

# Step 9: Output the final modified string
print(final_string)
