# Step 1: Read user input
inputLine = input().strip()  # Reading input and removing any trailing newline

# Step 2: Initialize variables
lengthOfInput = len(inputLine)  # Get length of the input string
maxLength = 0  # To track the length of the longest repeated substring

# Step 3: Check for repeated substrings
# Iterate over possible substring lengths
for currentLength in range(1, lengthOfInput):  # Start at 1 to avoid empty substring
    # Iterate over starting positions for the substring
    for startIndex in range(lengthOfInput - currentLength + 1):  # Ensure valid substring index
        substring = inputLine[startIndex:startIndex + currentLength]  # Extract the substring

        # Step 6: Check if the substring appears again after its position
        if inputLine.find(substring, startIndex + 1) != -1:  # Find substring starting after startIndex
            maxLength = currentLength  # Update maxLength if found
            break  # No need to check further for this length

# Step 7: Output the result
print(maxLength)  # Print the length of the longest repeated substring
