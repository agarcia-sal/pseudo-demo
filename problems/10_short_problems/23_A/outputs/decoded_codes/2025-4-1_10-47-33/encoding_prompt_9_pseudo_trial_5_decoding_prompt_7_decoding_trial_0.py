# Step 1: Get the Input
# Read a line of text from the user
input_string = input().strip()  # Removing any trailing newline character
stringLength = len(input_string)  # Store the length of the input string
longestRepeatedSubstringLength = 0  # Initialize to keep track of the maximum length found

# Step 2: Iterate Over Possible Substring Lengths
# For each possible substring length from 1 to stringLength - 1
for currentLength in range(1, stringLength):  
    # For each starting position from 0 to stringLength - currentLength
    for startPosition in range(stringLength - currentLength):  
        # Extract the substring from the current start position
        substring = input_string[startPosition:startPosition + currentLength]

        # Check if this substring appears again in the remainder of the string
        if substring in input_string[startPosition + 1:]:  # Search in the remainder of the string
            longestRepeatedSubstringLength = currentLength  # Update if a match is found
            break  # Exit the inner loop since we found a repeated substring

# Step 3: Output the Length
print(longestRepeatedSubstringLength)  # Print the result
