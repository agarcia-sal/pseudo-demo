# Read a line of input and remove the trailing newline character
input_line = input().strip()

# Determine the length of the input line
lengthOfLine = len(input_line)

# Initialize a variable to hold the length of the longest repeated substring
repeatedSubstringLength = 0

# Loop through each possible length of substring from 0 to lengthOfLine - 1
for substringLength in range(lengthOfLine):
    # Loop through each starting index for the substring
    for startIndex in range(lengthOfLine):
        # Extract the substring
        substring = input_line[startIndex:startIndex + substringLength]
        
        # Check if the substring can be found later in the input line
        if substring in input_line[startIndex + substringLength:]:
            repeatedSubstringLength = substringLength
            break  # Exit the inner loop if a repeated substring is found

# Output the length of the longest repeated substring
print(repeatedSubstringLength)
