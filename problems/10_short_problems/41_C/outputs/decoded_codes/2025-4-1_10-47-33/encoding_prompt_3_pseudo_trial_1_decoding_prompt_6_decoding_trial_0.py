# Step 1: Read the input string and prepare it for processing
input_string = input().strip()  # Remove any leading/trailing whitespace

# Step 2: Replace specific substrings for formatting
input_string = input_string.replace("dot", ".")  # Replace "dot" with "."
input_string = input_string.replace("at", "@")    # Replace "at" with "@"

# Step 3: Check and modify the first character if it's a period
if input_string and input_string[0] == ".":
    input_string = "dot" + input_string[1:]  # Prepend "dot" if the first character is "."

# Step 4: Initialize variables for processing the string
count_at = 0  # Counter for occurrences of '@' character
formatted_characters = []  # To hold processed characters

# Step 5: Modify the string further if it starts with '@'
if input_string and input_string[0] == "@":
    input_string = "at" + input_string[1:]  # Prepend "at" if the first character is "@"

# Step 6: Iterate through each character in the modified string
for character in input_string:
    if character == "@":  # Check if the current character is '@'
        if count_at > 0:  # If we already counted an '@'
            formatted_characters.append("at")  # Append "at"
        else:
            formatted_characters.append("@")  # Append "@"
        count_at += 1  # Increment the count of '@'
    else:
        formatted_characters.append(character)  # Append the character as is

# Step 7: Join the formatted characters into a single string
output_string = ''.join(formatted_characters)  # Join list into string

# Step 8: Final formatting for the output string
if output_string and output_string[-1] == ".":  # Check last character
    output_string = output_string[:-1] + "dot"  # Replace last character with "dot"

# Step 9: Output the final formatted string
print(output_string)  # Print the final output string
