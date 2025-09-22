inputLine = input().rstrip()  # Read a line of input and remove the last character
inputLength = len(inputLine)
resultValue = 0

# Iterate through each possible length of substrings
for substringLength in range(inputLength):
    
    # Check each starting position for the substring of given length
    for startIndex in range(inputLength):
        
        # Extract the substring from the current starting position
        substring = inputLine[startIndex:startIndex + substringLength]
        
        # Check if the substring can be found later in the string
        if inputLine.find(substring, startIndex + 1) != -1:
            
            # Update the resultValue to the current substring length
            resultValue = substringLength
            break  # Exit the inner loop once a match is found

# Output the maximum length of the found substring
print(resultValue)
