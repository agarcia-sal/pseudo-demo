# Read input from standard input and remove any surrounding whitespace
input_string = input().strip()

# Initialize an index for tracking the current position in the input string
index = 0

# Initialize an empty string to store the output result
result = ""

# While the index is less than the length of the input string
while index < len(input_string):
    
    # Check if the current character is a dot (.)
    if input_string[index] == '.':
        result += '0'  # Append '0' to result
        index += 1     # Increment index by 1

    # Check if the next character is also a dot (.)
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'  # Append '1' to result
        index += 2     # Increment index by 2

    # If the current character is not a dot and the next character is not a dot
    else:
        result += '2'  # Append '2' to result
        index += 2     # Increment index by 2

# Output the final result
print(result)
