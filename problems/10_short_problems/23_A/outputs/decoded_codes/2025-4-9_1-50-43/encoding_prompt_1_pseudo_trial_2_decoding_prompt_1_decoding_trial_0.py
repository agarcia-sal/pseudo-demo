# Read Input
inputLine = input().rstrip()  # Remove trailing newline character
textLength = len(inputLine)  # Length of the line of text
longestRepeatedLength = 0  # Initialize longest repeated length to zero

# Outer Loop
for currentLength in range(textLength):  # from 0 to textLength - 1
    # Inner Loop
    for startIndex in range(textLength):  # from 0 to textLength - 1
        # Define Substring
        currentSubstring = inputLine[startIndex:startIndex + currentLength]  # Substring
        
        # Check for Repetition
        if currentSubstring in inputLine[startIndex + 1:]:  # Check for repetition
            longestRepeatedLength = currentLength  # Update length of longest repetition
            break  # Exit inner loop since we found a repeat

# Output Result
print(longestRepeatedLength)  # Print the length of the longest repeating substring
