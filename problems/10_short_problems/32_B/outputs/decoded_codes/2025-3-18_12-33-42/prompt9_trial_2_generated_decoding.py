# Receive Input
input_string = input().strip()  # Read and remove surrounding whitespace

# Initialize Variables
index = 0  # Counter to track our position in the input string
result = ""  # String to store output numbers

# Process the Input
while index < len(input_string):
    if input_string[index] == '.':
        result += '0'  # Add '0' for a single dot
        index += 1  # Move to the next character
    else:
        if index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += '1'  # Add '1' for a pair of dots
            index += 2  # Move forward by 2 characters
        else:
            result += '2'  # Add '2' for any other character
            index += 2  # Move forward by 2 characters

# Output the Result
print(result)
