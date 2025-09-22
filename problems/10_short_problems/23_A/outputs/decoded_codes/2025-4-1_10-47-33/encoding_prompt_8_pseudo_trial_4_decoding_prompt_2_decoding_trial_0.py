# Step 1: Read input
inputLine = input().rstrip()  # Read input line from user and strip any trailing newline

# Step 2: Initialize variables
lengthOfInput = len(inputLine)  # Determine the length of the input string
maxLength = 0  # To track the length of the longest repeated substring

# Step 3: Check for repeated substrings
for currentLength in range(lengthOfInput):  # For each possible length
    for startIndex in range(lengthOfInput):  # For each starting position
        # Step 5: Extract substring
        substring = inputLine[startIndex:startIndex + currentLength]  # Extract substring

        # Step 6: Check if the substring appears again after its position
        if inputLine.find(substring, startIndex + 1) != -1:  # Check for repeat
            maxLength = currentLength  # Update maxLength
            break  # Exit inner loop as we found a repeat

# Step 7: Output the result
print(maxLength)
