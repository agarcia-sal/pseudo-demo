# Receive Input
inputLine = input().rstrip()  # Read a line of text and remove the newline character

# Initialize Variables
lengthOfLine = len(inputLine)  # Get the length of the input line
resultValue = 0  # This will hold the length of the longest repeating substring

# Loop through Possible Substring Lengths
for currentLength in range(lengthOfLine):  # Iterate through lengths from 0 to lengthOfLine - 1
    for currentIndex in range(lengthOfLine):  # Iterate through all character positions
        # Determine the substring start from currentIndex of length currentLength
        substring = inputLine[currentIndex:currentIndex + currentLength]
        # Check for Substring Reoccurrence
        if substring in inputLine[currentIndex + 1:]:  # Search in the remaining part of inputLine
            resultValue = currentLength  # Record the length of the found substring
            break  # Exit the inner loop as we found a reoccurring substring

# Output the Result
print(resultValue)  # Print the length of the longest repeating substring found
