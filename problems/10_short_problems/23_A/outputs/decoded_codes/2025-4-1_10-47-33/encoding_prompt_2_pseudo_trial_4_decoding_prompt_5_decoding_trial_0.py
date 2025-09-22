# Function to find the length of the longest repeating substring
def longest_repeating_substring():
    # Step 1: Receive input
    inputLine = input().rstrip()  # Read input and remove the newline character
    lengthOfLine = len(inputLine)  # Get the length of the input string
    resultValue = 0  # Initialize the result to 0

    # Step 3: Loop through possible substring lengths
    for currentLength in range(lengthOfLine):  # Iterate from 0 to lengthOfLine - 1
        for currentIndex in range(lengthOfLine):  # Iterate over each character position
            # Check if the substring length is valid
            if currentIndex + currentLength < lengthOfLine:  # Ensure we don't go out of bounds
                substring = inputLine[currentIndex:currentIndex + currentLength + 1]  # Extract substring
                # Step 4: Check for substring reoccurrence
                if substring in inputLine[currentIndex + 1:]:  # Check if substring occurring again
                    resultValue = currentLength + 1  # Update resultValue to the length of the found substring
                    break  # Exit inner loop as we found a repeating substring
        # If we found a repeating substring of the currentLength, no need to check larger lengths
        if resultValue > 0:  
            break 

    # Step 5: Output the result
    print(resultValue)  # Output the length of the longest repeated substring

# Note: To test this function, simply call `longest_repeating_substring()` and provide input.
