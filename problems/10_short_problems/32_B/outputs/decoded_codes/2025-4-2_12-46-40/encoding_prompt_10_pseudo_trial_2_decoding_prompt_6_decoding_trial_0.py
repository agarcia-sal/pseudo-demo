# Begin execution of the program

# Declare variables
input_string = ""  # This will hold the input string
index = 0  # This will be used as a counter to traverse the string
result_string = ""  # This will hold the final result

# Read a line of input and remove surrounding whitespace
input_string = input().strip()

# Loop through characters in the string until the end is reached
while index < len(input_string):
    # Check the current character for encoding
    if input_string[index] == '.':
        # If it's a single dot, append '0' to the result
        result_string += '0'
        index += 1  # Increment index by 1
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        # If next character is a dot, append '1' to the result
        result_string += '1'
        index += 2  # Increment index by 2
    else:
        # In all other cases, append '2' to the result
        result_string += '2'
        index += 2  # Increment index by 2

# Output the final result
print(result_string)
