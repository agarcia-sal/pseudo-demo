# Begin the program

# Read a line of input from the user and remove the last character
inputLine = input()[:-1]  # Read input and remove the last character
inputLength = len(inputLine)  # Get the length of the input
resultValue = 0  # Initialize result value to store maximum length of repeated substring

# Iterate through each possible length of substrings
for substringLength in range(inputLength):  # range goes from 0 to inputLength - 1

    # Check each starting position for the substring of given length
    for startIndex in range(inputLength):  # range from 0 to inputLength - 1

        # Extract the substring from the current starting position
        substring = inputLine[startIndex:startIndex + substringLength]

        # Check if the substring can be found later in the string
        if inputLine.find(substring, startIndex + 1) != -1:  # Find the substring starting from the next index
            # Update the resultValue to the current substring length
            resultValue = substringLength
            break  # Exit the inner loop once a match is found

# Output the maximum length of the found substring
print(resultValue)  # Print the result value

# End the program
