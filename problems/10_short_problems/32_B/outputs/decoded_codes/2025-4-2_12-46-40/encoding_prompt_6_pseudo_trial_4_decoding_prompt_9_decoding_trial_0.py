# Read input from standard input and remove any extra spaces or newline characters
input_string = input().strip()

# Initialize index and output string
index = 0
output_string = ""

# Process the input string while there are still characters remaining
while index < len(input_string):
    # Check if the current character is a single dot
    if input_string[index] == '.':
        output_string += '0'  # Append '0' to outputString
        index += 1  # Move to the next character

    # Check if the next character is also a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        output_string += '1'  # Append '1' to outputString
        index += 2  # Move past the pair of dots

    # If neither case is met, we have a dot followed by something else
    else:
        output_string += '2'  # Append '2' to outputString
        index += 2  # Move past the pair of characters

# Output the final result
print(output_string)
