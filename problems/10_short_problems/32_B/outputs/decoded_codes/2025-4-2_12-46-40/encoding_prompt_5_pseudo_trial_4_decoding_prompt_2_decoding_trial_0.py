# Step 1: Accept a string of characters from the user
input_string = input()

# Step 2: Initialize variables
i = 0
decodedOutput = ""

# Step 3: Process input string
while i < len(input_string):
    if input_string[i] == '.':
        decodedOutput += '0'
        i += 1
    elif i + 1 < len(input_string) and input_string[i + 1] == '.':
        decodedOutput += '1'
        i += 2
    else:  # This covers the case where the current character is a hyphen
        decodedOutput += '2'
        i += 2

# Step 4: Output result
print(decodedOutput)
