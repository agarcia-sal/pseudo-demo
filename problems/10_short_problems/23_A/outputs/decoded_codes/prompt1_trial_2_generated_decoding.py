# Begin

# Read a line of input and remove the trailing newline character
inputLine = input().strip()  # Input is read from standard input
lengthOfInput = len(inputLine)
resultValue = 0

# Iterate over possible substring lengths from 0 to lengthOfInput - 1
for substringLength in range(lengthOfInput):  # This will generate values from 0 to lengthOfInput - 1
    # Check all starting positions of the substring
    for startingIndex in range(lengthOfInput):  # This will generate starting positions from 0 to lengthOfInput - 1
        # Extract the current substring based on the length and index
        currentSubstring = inputLine[startingIndex:startingIndex + substringLength]  # Extracts the substring

        # Check if this substring exists later in the input line
        if currentSubstring and inputLine.find(currentSubstring, startingIndex + 1) != -1:
            # Update the result to the current substring length
            resultValue = substringLength
            
            # Break the inner loop since we found a match
            break

    # If a match was found, exit the outer loop as well
    if resultValue != 0:
        break

# Output the length of the longest found substring that repeats
print(resultValue)

# End
