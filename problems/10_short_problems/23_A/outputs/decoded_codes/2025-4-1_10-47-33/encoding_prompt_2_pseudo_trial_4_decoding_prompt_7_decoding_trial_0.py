# Step 1: Receive Input
# Read a line of text from standard input
inputLine = input().strip()  # Remove any surrounding whitespace/newline

# Step 2: Initialize Variables
lengthOfLine = len(inputLine)  # Get the length of the input line
resultValue = 0  # Initialize result value to 0

# Step 3: Loop through PossibleSubstringLengths
# Loop for each possible substring length from 1 to lengthOfLine - 1
for currentLength in range(1, lengthOfLine):  # Start from 1 to avoid empty substring
    # Step 4: Check for Substring Reoccurrence
    for currentIndex in range(lengthOfLine - currentLength):  # Avoid overflow
        # Get the current substring
        substring = inputLine[currentIndex: currentIndex + currentLength]
        # Check if the substring can be found again in inputLine
        if substring in inputLine[currentIndex + 1:]:
            resultValue = currentLength  # Update resultValue with the length of found substring
            break  # Exit the inner loop as we found a reoccurring substring

# Step 5: Output the Result
print(resultValue)  # Print the longest length of the substring that occurs more than once
