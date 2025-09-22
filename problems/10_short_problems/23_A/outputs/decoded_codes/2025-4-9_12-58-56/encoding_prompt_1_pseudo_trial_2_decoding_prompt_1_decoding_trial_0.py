# Step 1: Start Program

# Step 2: Read Input
inputString = input().rstrip()  # Get a line of text and remove the newline character

# Step 3: Initialize Variables
lengthOfInput = len(inputString)  # Calculate the length of inputString
longestRepeatedLength = 0  # Variable to store the longest repeated length

# Step 4: Loop Through Possible Substring Lengths
for currentLength in range(lengthOfInput):  # For each length from 0 to lengthOfInput - 1
    # Inner Loop for Substring Checking
    for startIndex in range(lengthOfInput):  # For each starting index from 0 to lengthOfInput - 1
        currentSubstring = inputString[startIndex:startIndex + currentLength]  # Extract substring
        
        # Check if currentSubstring appears again in inputString after startIndex
        if currentSubstring in inputString[startIndex + 1:]:  # Check in the remainder of the string
            longestRepeatedLength = currentLength  # Update longestRepeatedLength
            break  # Exit inner loop since a repeat was found

# Step 5: Output Result
print(longestRepeatedLength)  # Print the length of the longest repeated substring found
