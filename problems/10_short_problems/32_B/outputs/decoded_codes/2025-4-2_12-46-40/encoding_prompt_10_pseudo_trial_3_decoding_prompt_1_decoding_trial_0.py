# Step 1: Read input and initialize variables
inputString = input().strip()  # Read input and remove trailing spaces
index = 0  # Initialize index
answer = ""  # Initialize answer as an empty string

# Step 2: Process each character in the input string
while index < len(inputString):  # While index is less than the length of inputString
    if inputString[index] == '.':  # If the character at index is '.'
        answer += '0'  # Append '0' to answer
        index += 1  # Increment index by 1
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Check next character
        answer += '1'  # Append '1' to answer
        index += 2  # Increment index by 2
    else:  # If no conditions matched
        answer += '2'  # Append '2' to answer
        index += 2  # Increment index by 2

# Step 3: Output the result
print(answer)  # Print the answer
