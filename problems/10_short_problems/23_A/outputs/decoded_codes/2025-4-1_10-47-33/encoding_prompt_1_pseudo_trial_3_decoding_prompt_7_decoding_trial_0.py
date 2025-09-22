# Function to find the maximum length of a repeated substring
def find_max_repeated_substring_length():
    # Read a line of input from the user and remove the last character
    inputLine = input().strip()[:-1]  # Get input and remove last character
    inputLength = len(inputLine)  # Get the length of the input string
    resultValue = 0  # Initialize variable to store the maximum length of repeated substring
    
    # Iterate through each possible length of substrings
    for substringLength in range(1, inputLength):  # Start from 1 to avoid empty substring
        # Check each starting position for the substring of given length
        for startIndex in range(inputLength - substringLength + 1):
            # Extract the substring from the current starting position
            substring = inputLine[startIndex:startIndex + substringLength]
            
            # Check if the substring can be found later in the string
            if substring in inputLine[startIndex + 1:]:  # Search from next character onward
                # Update the resultValue to the current substring length
                resultValue = substringLength
                break  # Exit the inner loop once a match is found
    
    # Output the maximum length of the found substring
    print(resultValue)


# Run the function to execute the logic
find_max_repeated_substring_length()
