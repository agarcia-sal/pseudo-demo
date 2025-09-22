# Define Input
input_string = input()

# Initialize Variables
i = 0
decodedOutput = ""

# Process Input String
while i < len(input_string):
    if input_string[i] == '.':
        decodedOutput += '0'
        i += 1
    elif i + 1 < len(input_string) and input_string[i + 1] == '.':
        decodedOutput += '1'
        i += 2
    else:  # This implies the current character is a hyphen
        decodedOutput += '2'
        i += 2

# Output Result
print(decodedOutput)
