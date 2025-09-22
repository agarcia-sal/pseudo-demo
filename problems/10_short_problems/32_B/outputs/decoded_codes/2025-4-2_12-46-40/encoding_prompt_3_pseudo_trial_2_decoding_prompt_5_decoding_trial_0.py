# Read input from standard input
input_string = input().strip()  # Remove whitespace from input

# Initialize an index to track position in the string
index = 0
# Initialize a string to store the output
output_string = ""

# While there are more characters to process in the input string
while index < len(input_string):
    # Check the current character
    if input_string[index] == '.':
        # If current character is '.', append '0' to output_string
        output_string += '0'
        index += 1

    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        # If next character is '.', append '1' to output_string
        output_string += '1'
        index += 2
        
    else:
        # Otherwise, append '2' to output_string
        output_string += '2'
        index += 2

# Output the final result
print(output_string)
