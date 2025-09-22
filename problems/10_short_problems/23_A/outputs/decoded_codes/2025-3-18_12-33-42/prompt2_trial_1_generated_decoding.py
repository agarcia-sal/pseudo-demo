# Start the program.

# Read a line of input from the standard input, removing the trailing newline character.
inputLine = input().rstrip('\n')

# Determine the length of inputLine and store it in a variable called lengthOfInput.
lengthOfInput = len(inputLine)

# Initialize a variable called resultValue to zero.
resultValue = 0

# Begin a loop that iterates over each possible substring length l.
for l in range(lengthOfInput):
    # Begin another loop that iterates over each starting position i for substrings of length l.
    for i in range(lengthOfInput - l):
        # Extract the substring from inputLine starting at position i with length l.
        substring = inputLine[i:i + l + 1]  # l + 1 because we want length 'l'
        
        # Check if this substring can be found elsewhere in inputLine starting from position i + 1.
        if inputLine.find(substring, i + 1) != -1:
            # If the substring is found, update resultValue to the current length l.
            resultValue = l + 1  # l + 1 because we want the actual length
            # Exit the inner loop.
            break

# Output the value of resultValue, which represents the length of the longest duplicated substring found in inputLine.
print(resultValue)

# End the program.
