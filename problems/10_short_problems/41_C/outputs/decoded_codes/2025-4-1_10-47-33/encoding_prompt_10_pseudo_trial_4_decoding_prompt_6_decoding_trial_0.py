# Start of the program

# Read input from standard input
input_string = input()  # Read a line from standard input
input_string = input_string.strip()  # Remove whitespace from the beginning and end

# Replace occurrences of 'dot' with '.'
input_string = input_string.replace('dot', '.')
# Replace occurrences of 'at' with '@'
input_string = input_string.replace('at', '@')

# Check if the first character is a dot
if input_string.startswith('.'):
    input_string = 'dot' + input_string[1:]  # Concatenate 'dot' with substring from index 1

# Initialize counter and list to store modified characters
counter = 0  # This replaces the 'co' variable
result_list = []  # This will store the final characters
length = 0  # This variable can be used for other purposes if needed

# Check if the first character is an at symbol
if input_string.startswith('@'):
    input_string = 'at' + input_string[1:]  # Concatenate 'at' with substring from index 1

# Iterate over each character in the input string
for character in input_string:
    if character == '@':
        # Check if we have seen an '@' before
        if counter > 0:
            result_list.append('at')  # Append 'at' to the list
            counter = 1  # Update counter
        else:
            result_list.append('@')  # Append '@' to the list
            counter = 1  # Update counter
    else:
        result_list.append(character)  # Append the character to the list

# Join the list into a single string
result_string = ''.join(result_list)

# Check if the last character is a dot
if result_string.endswith('.'):
    result_string = result_string[:-1] + 'dot'  # Remove the last character and append 'dot'

# Output the final result
print(result_string)

# End of the program
