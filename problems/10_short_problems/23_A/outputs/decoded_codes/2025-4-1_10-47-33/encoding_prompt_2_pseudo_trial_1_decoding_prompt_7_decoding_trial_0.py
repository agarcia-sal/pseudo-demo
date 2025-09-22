# Read input: Take a single line of input from the user and remove the trailing newline character.
input_string = input().strip()

# Determine length: Calculate the length of the input string.
stringLength = len(input_string)

# Initialize variable: Set a variable to track the length of the longest repeated substring.
repeatedSubstringLength = 0

# Outer loop: For each possible substring length from 1 to stringLength - 1
for substringLength in range(1, stringLength):  # Start from 1 to avoid 0-length substrings
    # Inner loop: For each possible starting index within the string
    for startIndex in range(stringLength - substringLength + 1):
        # Extract the substring starting from the current index
        substring = input_string[startIndex:startIndex + substringLength]
        
        # Check if this substring appears again in the string after the current index
        if substring in input_string[startIndex + 1:]:
            # If the substring is found again, update the repeatedSubstringLength
            repeatedSubstringLength = substringLength
            # Exit the inner loop because a repeat has been found
            break

# Output result: Display the length of the longest repeated substring found
print(repeatedSubstringLength)
