# The main logic begins here

# Read input string from standard input and remove any leading/trailing whitespace
input_string = input().strip()

# Initialize index and output result
index = 0
result = ""

# Loop through the string as long as the index is less than the length of the input_string
while index < len(input_string):
    # Check if the current character is a dot
    if input_string[index] == '.':
        # Append '0' to the result
        result += '0'
        # Move to the next character
        index += 1
    else:
        # Check if the next character is also a dot and is in bounds
        if index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Append '1' to the result
            result += '1'
            # Move the index forward by two characters
            index += 2
        else:
            # If the next character is not a dot, append '2' to the result
            result += '2'
            # Move the index forward by two characters
            index += 2

# Output the final result
print(result)
