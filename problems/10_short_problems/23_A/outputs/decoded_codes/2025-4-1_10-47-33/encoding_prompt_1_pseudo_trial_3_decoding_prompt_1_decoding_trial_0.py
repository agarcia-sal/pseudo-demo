# BEGIN

# Read a line of input from the user and remove the last character
inputLine = input()[:-1]  # Read input and remove last character
inputLength = len(inputLine)
resultValue = 0

# Iterate through each possible length of substrings
for substringLength in range(inputLength):  # 0 to inputLength - 1 inclusive

    # Check each starting position for the substring of given length
    for startIndex in range(inputLength):  # 0 to inputLength - 1 inclusive

        # Extract the substring from the current starting position
        substring = inputLine[startIndex:startIndex + substringLength + 1]  # Extract substring

        # Check if the substring can be found later in the string
        if inputLine.find(substring, startIndex + 1) != -1:  # Checking for substring after startIndex
            # Update the resultValue to the current substring length
            resultValue = substringLength
            break  # Exit the inner loop once a match is found

# Output the maximum length of the found substring
print(resultValue)

# END
