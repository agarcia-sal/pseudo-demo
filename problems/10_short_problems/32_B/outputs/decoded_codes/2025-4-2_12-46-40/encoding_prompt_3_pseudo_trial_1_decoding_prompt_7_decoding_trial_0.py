# BEGIN

# Read input from standard input and remove any surrounding whitespace
inputString = input().strip()

# Initialize an index for tracking the current position in the input string
index = 0

# Initialize an empty string to store the output result
result = ""

# While the index is less than the length of the input string
while index < len(inputString):
    
    # Check if the current character is a dot (.)
    if inputString[index] == '.':
        # Append '0' to result
        result += '0'
        # Increment index by 1
        index += 1
        
    # Check if the next character is also a dot (.)
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        # Append '1' to result
        result += '1'
        # Increment index by 2
        index += 2
        
    # If the current character is not a dot and the next character is not a dot
    else:
        # Append '2' to result
        result += '2'
        # Increment index by 2
        index += 2

# Output the final result
print(result)

# END
