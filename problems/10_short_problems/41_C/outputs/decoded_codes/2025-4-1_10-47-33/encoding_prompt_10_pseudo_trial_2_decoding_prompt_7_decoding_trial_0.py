# Read input from standard input, trimming any whitespace
input_string = input().strip()

# Replace substrings as specified
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Check if the first character is a period and prepend "dot" if needed
if input_string and input_string[0] == '.':
    input_string = "dot" + input_string[1:]

# Initialize necessary variables
count_at = 0  # Used to track occurrences of the at symbol
result_list = []  # To store processed characters
length = 0  # Not used later, but initialized

# Handle case where the first character is '@'
if input_string and input_string[0] == '@':
    input_string = "at" + input_string[1:]

# Process each character in the input string
for character in input_string:
    if character == '@':  # Check if the character is '@'
        if count_at > 0:  # If '@' has already been encountered
            result_list.append("at")  # Append "at" to the list
            count_at = 1  # Update count
        else:
            result_list.append('@')  # Append '@' only
            count_at = 1  # Update count
    else:
        result_list.append(character)  # Append the current character

# Join all elements in the result list to form the processed string
processed_string = ''.join(result_list)

# Check if the last character is a period and replace it with "dot" if needed
if processed_string and processed_string[-1] == '.':
    processed_string = processed_string[:-1] + "dot"

# Output the final processed string
print(processed_string)
