def find_longest_repeating_substring():
    # Step 1: Receive Input
    inputLine = input().rstrip()  # Read input and remove newline character

    # Step 2: Initialize Variables
    lengthOfLine = len(inputLine)  # Get the length of inputLine
    resultValue = 0  # Initialize result variable to hold the longest substring length

    # Step 3: Loop through PossibleSubstringLengths
    for currentLength in range(lengthOfLine):  # from 0 to lengthOfLine - 1
        for currentIndex in range(lengthOfLine):  # from 0 to lengthOfLine - 1
            # Step 4: Check for Substring Reoccurrence
            substring = inputLine[currentIndex:currentIndex + currentLength]  # Extract substring
            if substring and substring in inputLine[currentIndex + 1:]:  # Check for reoccurrence
                resultValue = currentLength  # Update resultValue if found
                break  # Exit the inner loop as we found a repeating substring

    # Step 5: Output the Result
    print(resultValue)

# Call the function to execute
find_longest_repeating_substring()
