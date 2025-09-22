# Step 1: Initialize Program
# Read input line and remove the trailing newline character
inputLine = input().strip()
# Store the length of the input line
length = len(inputLine)
# Initialize result to 0 to hold the length of the longest repeating substring
result = 0

# Step 2: Main Loop
# Iterate through all possible substring lengths from 0 to length - 1
for subLength in range(1, length):  # Start from 1 since a length of 0 is not meaningful
    # Iterate through all starting positions in the input line
    for startIndex in range(length - subLength):
        # Extract the substring of inputLine starting at startIndex with the length subLength
        substring = inputLine[startIndex:startIndex + subLength]
        # Check if this substring appears again in inputLine starting from position startIndex + 1
        if substring in inputLine[startIndex + 1:]:
            # If found, update result with the current subLength
            result = subLength
            # Break out of the inner loop to test the next substring length
            break

# Step 3: Output the Result
# Print the value of result, which holds the length of the longest repeating substring
print(result)
