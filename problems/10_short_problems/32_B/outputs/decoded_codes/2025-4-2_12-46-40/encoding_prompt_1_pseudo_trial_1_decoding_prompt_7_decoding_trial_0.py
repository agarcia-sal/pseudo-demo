# Convert a Given String Representation to a Numeric String

# Step 1: Start the program
# Step 2: Read a line of input from standard input and remove leading/trailing whitespace
inputString = input().strip()

# Step 3: Initialize an index variable to keep track of the current character position
currentIndex = 0

# Step 4: Initialize an empty string to hold the output result
result = ""

# Step 5: Process the input string until the end
while currentIndex < len(inputString):
    # If the character at currentIndex is a dot ('.'):
    if inputString[currentIndex] == '.':
        result += '0'  # Append '0' to result
        currentIndex += 1  # Increment index by 1
    
    # Else If the next character is also a dot:
    elif currentIndex + 1 < len(inputString) and inputString[currentIndex + 1] == '.':
        result += '1'  # Append '1' to result
        currentIndex += 2  # Increment index by 2
    
    # Else (for any other character):
    else:
        result += '2'  # Append '2' to result
        currentIndex += 2  # Increment index by 2

# Step 6: Output the value of result
print(result)

# Step 7: End the program
