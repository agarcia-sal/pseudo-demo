# 1. Read Input
input_line = input().rstrip('\n')  # Read a line and remove the trailing newline
lengthOfLine = len(input_line)       # Store the length of the input line

# 2. Initialize Result Variable
repeatedSubstringLength = 0           # Variable to track the longest repeated substring length

# 3. Outer Loop for Substring Lengths
for currentLength in range(lengthOfLine):  # Iterate from 0 to lengthOfLine - 1
    # Inner Loop for Starting Points
    for startIndex in range(lengthOfLine):  # Iterate over each starting position
        # Extract substring
        substring = input_line[startIndex:startIndex + currentLength]  # Get the substring

        # Check if this substring appears in the remaining part of the line
        if substring in input_line[startIndex + 1:]:  # Check in the remaining part of the line
            repeatedSubstringLength = currentLength  # Update the length of repeated substring
            break  # Exit the inner loop to check the next length

# 4. Output Result
print(repeatedSubstringLength)  # Output the length of the longest repeated substring found
