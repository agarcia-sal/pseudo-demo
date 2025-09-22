# 1. Read Input
input_string = input()  # Input string from user
stringLength = len(input_string)  # Length of the string
longestRepeatingSubstringLength = 0  # Initialize the length of the longest repeating substring

# 2. Iterate Through Substring Lengths
for currentLength in range(1, stringLength):  # currentLength starts from 1 to stringLength-1
    for startIndex in range(stringLength - currentLength + 1):  # Ensure we don't go out of range
        # 1. Extract Substring
        substring = input_string[startIndex:startIndex + currentLength]  # Get the substring

        # 2. Search for Repeats
        if substring in input_string[startIndex + 1:]:  # Look in the remaining part of the string
            longestRepeatingSubstringLength = currentLength  # Update the length found
            break  # Exit the inner loop

# 3. Output Result
print(longestRepeatingSubstringLength)  # Print the longest repeating substring length
