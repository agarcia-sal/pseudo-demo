# Step 1: Receive Input
input_string = input().strip()  # Read input and remove any leading or trailing whitespace

# Step 2: Replace Text Representations
input_string = input_string.replace("dot", ".")  # Replace "dot" with "."
input_string = input_string.replace("at", "@")    # Replace "at" with "@"

# Step 3: Check and Adjust Starting Character
if input_string.startswith("."):  # Check if the first character is "."
    input_string = "dot" + input_string  # Prepend "dot"

# Step 4: Initialize Variables
count = 0  # Counter for occurrences of "at"
characters = []  # List to store processed characters

# Step 5: Check for '@' Symbol at Start
if input_string.startswith("@"):  # Check if the first character is "@"
    characters.append("at")  # Prepend "at" to the characters list
    count = 1  # Set count as 1 to indicate the first 'at' handled
else:
    count = 0  # Reset count if not starting with "at"

# Step 6: Process Each Character in the String
for current_character in input_string:
    if current_character == "@":  # Check if the current character is "@"
        if count > 0:  # If we’ve already seen an "at"
            characters.append("at")  # Add "at" to list
            count = 1  # Reset count
        else:
            characters.append("@")  # Add "@" to list
            count = 1  # Set count to indicate "at" has been handled
    else:
        characters.append(current_character)  # Add other characters to list

# Step 7: Join Processed Characters
final_string = ''.join(characters)  # Combine characters into a single string

# Step 8: Handle Trailing Periods
if final_string.endswith("."):  # Check if final string ends with "."
    final_string = final_string[:-1] + "dot"  # Replace last "." with "dot"

# Step 9: Output the Final String
print(final_string)  # Print the processed final string
