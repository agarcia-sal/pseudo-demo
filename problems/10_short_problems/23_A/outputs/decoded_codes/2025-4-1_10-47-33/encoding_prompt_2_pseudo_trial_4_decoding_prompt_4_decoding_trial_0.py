# Receive Input
inputLine = input().rstrip()  # Read a line of text and remove any trailing newline

# Initialize Variables
lengthOfLine = len(inputLine)
resultValue = 0  # This will hold the length of the longest substring that reoccurs

# Loop through Possible Substring Lengths
for currentLength in range(lengthOfLine):  # currentLength from 0 to lengthOfLine - 1
    for currentIndex in range(lengthOfLine):  # currentIndex from 0 to lengthOfLine - 1
        # Check to ensure the substring doesn't go out of bounds
        if currentIndex + currentLength < lengthOfLine:
            substring = inputLine[currentIndex:currentIndex + currentLength + 1]  # Get the substring
            # Check for reoccurrence
            if substring in inputLine[currentIndex + 1:]:  # Look for the substring after its first occurrence
                resultValue = currentLength + 1  # Record the length of the found substring
                break  # Exit the inner loop immediately as we found a recurring substring
    if resultValue > 0:  # If a substring has been found, break the outer loop as well
        break

# Output the Result
print(resultValue)
