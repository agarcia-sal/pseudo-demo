# Step 1: Read Input
input_string = input().strip()  # Read input and remove leading/trailing whitespace

# Step 2: Replace Substrings
input_string = input_string.replace("dot", ".")  # Replace "dot" with "."
input_string = input_string.replace("at", "@")    # Replace "at" with "@"

# Step 3: Check Starting Character
if input_string and input_string[0] == '.':
    input_string = "dot" + input_string[1:]  # Prepend "dot" if the first character is "."

# Step 4: Initialize Variables
count_at = 0  # Count occurrences of '@'
result_list = []  # List to store processed characters

# Step 5: Handle Starting Character for the '@'
if input_string and input_string[0] == '@':
    input_string = "at" + input_string[1:]  # Prepend "at" if the first character is "@"

# Step 6: Process Each Character
for character in input_string:
    if character == '@':
        if count_at > 0:  # If already encountered an '@'
            result_list.append("at")  # Append "at" instead of '@'
            count_at = 1  # Set count_at to indicate '@' was added
        else:
            result_list.append('@')  # Append the '@'
            count_at = 1  # Increment count
    else:
        result_list.append(character)  # Append non-@ characters

# Step 7: Join Result
processed_string = ''.join(result_list)  # Join list into a string

# Step 8: Check Ending Character
if processed_string and processed_string[-1] == '.':
    processed_string = processed_string[:-1] + "dot"  # Replace last character '.' with "dot"

# Step 9: Output the Result
print(processed_string)  # Print the final processed string
