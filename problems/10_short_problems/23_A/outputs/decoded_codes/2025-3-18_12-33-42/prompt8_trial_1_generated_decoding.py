# Step 1: Read Input
inputString = input()

# Step 2: Initialize Variables
lengthOfString = len(inputString)
longestRepeatedSubstringLength = 0

# Step 3: Outer Loop for Substring Length
for substringLength in range(lengthOfString):
    # Step 4: Inner Loop for Starting Index of Substring
    for startIndex in range(lengthOfString):
        # Step 5: Extract Substring
        currentSubstring = inputString[startIndex:startIndex + substringLength + 1]
        
        # Step 6: Find Substring in String
        if inputString.find(currentSubstring, startIndex + 1) != -1:
            longestRepeatedSubstringLength = substringLength + 1
            break  # Exit the inner loop since the current substring has been found

# Step 8: Output Result
print(longestRepeatedSubstringLength)


def longest_repeated_substring(inputString):
    lengthOfString = len(inputString)
    longestRepeatedSubstringLength = 0

    for substringLength in range(lengthOfString):
        seen_substrings = set()
        for startIndex in range(lengthOfString):
            currentSubstring = inputString[startIndex:startIndex + substringLength + 1]
            if currentSubstring in seen_substrings:
                longestRepeatedSubstringLength = substringLength + 1
                break  # Exit inner loop after finding the repeated substring
            seen_substrings.add(currentSubstring)

    return longestRepeatedSubstringLength

# Read input and output result
inputString = input()
print(longest_repeated_substring(inputString))
