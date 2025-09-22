# BEGIN

# Read input from standard input
inputString = input()  # Read input without prompts
inputString = inputString.replace(" ", "")  # Remove whitespace from inputString

# Initialize an index to track position in the string
index = 0
# Initialize a string to store the output
outputString = ""

# While there are more characters to process in the input string
while index < len(inputString):

    # Check the current character
    if inputString[index] == '.':
        # If the current character is '.', append '0' to outputString
        outputString += '0'
        index += 1

    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        # If the next character is '.', append '1' to outputString
        outputString += '1'
        index += 2  # Move past both characters

    else:
        # Otherwise, append '2' to outputString
        outputString += '2'
        index += 2  # Move past both characters

# Output the final result
print(outputString)

# END
