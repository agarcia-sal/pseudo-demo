# Function to find the length of the longest repeated substring
def longest_repeated_substring():
    # Step 1: Read input
    inputLine = input().strip()

    # Step 2: Initialize variables
    lengthOfInput = len(inputLine)
    maxLength = 0  # To track the length of the longest repeated substring

    # Step 3: Check for repeated substrings
    for currentLength in range(1, lengthOfInput):  # Iterate from 1 to lengthOfInput - 1
        for startIndex in range(lengthOfInput - currentLength + 1):  # Ensure we don't exceed the string length
            substring = inputLine[startIndex:startIndex + currentLength]

            # Step 6: Check if the substring appears again after its position
            if inputLine.find(substring, startIndex + 1) != -1:
                maxLength = currentLength  # Update maxLength
                break  # No need to check further for this length

    # Step 7: Output the result
    print(maxLength)

# Invoke the function to execute
longest_repeated_substring()
