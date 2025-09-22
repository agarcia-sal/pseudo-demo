# Read Input
input_string = input()
stringLength = len(input_string)
longestRepeatingSubstringLength = 0

# Iterate Through Substring Lengths
for currentLength in range(stringLength):
    for startIndex in range(stringLength):
        
        # Extract Substring
        if startIndex + currentLength <= stringLength:  # Make sure the substring fits
            substring = input_string[startIndex:startIndex + currentLength]
            
            # Search for Repeats
            if substring in input_string[startIndex + 1:]:
                longestRepeatingSubstringLength = currentLength

# Output Result
print(longestRepeatingSubstringLength)
