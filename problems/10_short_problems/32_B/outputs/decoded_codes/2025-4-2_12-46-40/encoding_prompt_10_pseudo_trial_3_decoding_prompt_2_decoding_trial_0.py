# Step 1: Read input and initialize variables
inputString = input().strip()  # Reading input and removing trailing spaces
index = 0                       # Initializing index
answer = ""                     # Initializing answer as an empty string

# Step 2: Process each character in the input string
while index < len(inputString):  # Loop until the index is less than the length of inputString
    if inputString[index] == '.':  # Check if the current character is '.'
        answer += '0'               # Append '0' to answer
        index += 1                  # Increment index by 1
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Check if next character is '.'
        answer += '1'               # Append '1' to answer
        index += 2                  # Increment index by 2
    else:                           # Else case
        answer += '2'               # Append '2' to answer
        index += 2                  # Increment index by 2

# Step 3: Output the result
print(answer)                     # Print the final result
