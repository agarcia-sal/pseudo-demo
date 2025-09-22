def find_length_of_longest_repeated_substring():
    # Step 1: Read input and remove newline character
    inputString = input().strip()
    
    # Step 2: Determine the length of the input string
    lengthOfInputString = len(inputString)
    
    # Step 3: Initialize variable to track the longest repeated substring length
    longestRepeatedSubstringLength = 0

    # Step 4: Loop through each possible length of substrings
    for currentLength in range(1, lengthOfInputString):
        # Step 5: Check each substring's starting position
        found = False  # To check if we found a repeated substring
        for startPosition in range(lengthOfInputString - currentLength + 1):
            # Step 6: Extract the substring
            substring = inputString[startPosition:startPosition + currentLength]

            # Step 7: Check for repeated occurrence
            if substring in inputString[startPosition + 1:]:
                # Step 8: Update longest found length
                longestRepeatedSubstringLength = currentLength
                found = True
                break  # Exit the inner loop if we found a repeated substring
        
        # Step 9: If we found a repeated substring, go to the next length
        if found:
            continue
            
    # Step 10: Output the result
    print(longestRepeatedSubstringLength)

# You can call the function to test its functionality
find_length_of_longest_repeated_substring()
