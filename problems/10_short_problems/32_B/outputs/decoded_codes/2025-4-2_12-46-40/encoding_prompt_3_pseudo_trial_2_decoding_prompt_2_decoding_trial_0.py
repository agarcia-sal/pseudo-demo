# Read input from standard input
inputString = input().strip()  # Remove whitespace from inputString

# Initialize an index to track position in the string
index = 0
# Initialize a string to store the output
outputString = ""

# While there are more characters to process in the input string
while index < len(inputString):
    
    # Check the current character
    if inputString[index] == '.':
        # If current character is '.', append '0' to outputString
        outputString += '0'
        index += 1

    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        # If the next character is '.' then, append '1' to outputString
        outputString += '1'
        index += 2
        
    else:
        # Otherwise, append '2' to outputString
        outputString += '2'
        index += 2

# Output the final result
print(outputString)
