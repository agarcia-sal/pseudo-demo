# Read a line of input and remove any whitespace
input_string = input().strip()

# Initialize index and result string
index = 0
result = ""

# Loop until the end of the input string is reached
while index < len(input_string):
    # Check if the current character is a single dot
    if input_string[index] == '.':
        result += '0'  # Append '0' to result
        index += 1     # Increment index by 1
    else:
        # Check the next character to determine the value to append
        if index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += '1'  # Append '1' to result
            index += 2     # Increment index by 2
        else:
            result += '2'  # Append '2' to result
            index += 2     # Increment index by 2

# Output the final result
print(result)
