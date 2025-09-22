# Step 1: Receive Input
inputLine = input().strip()  # Read input and remove newline character

# Step 2: Initialize Variables
lengthOfLine = len(inputLine)  # Get the length of the input line
resultValue = 0  # Initialize the result variable

# Step 3: Loop through Possible Substring Lengths
for currentLength in range(lengthOfLine):  # From 0 to lengthOfLine - 1
    for currentIndex in range(lengthOfLine):  # For each character position
        # Step 4: Check for Substring Reoccurrence
        # Define the substring
        substring = inputLine[currentIndex:currentIndex + currentLength]

        # Only check if currentLength is greater than 0
        if currentLength > 0 and substring in inputLine[currentIndex + 1:]:
            resultValue = currentLength  # Update resultValue
            break  # Exit inner loop as we found a reoccurrence

# Step 5: Output the Result
print(resultValue)  # Print the length of the longest reoccurring substring
