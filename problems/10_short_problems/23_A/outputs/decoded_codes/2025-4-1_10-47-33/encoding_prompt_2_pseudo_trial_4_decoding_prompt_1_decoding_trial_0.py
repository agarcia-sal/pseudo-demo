# 1. Receive Input:
inputLine = input()  # Read input
inputLine = inputLine[:-1]  # Remove last character (newline)

# 2. Initialize Variables:
lengthOfLine = len(inputLine)  # Length of the input line
resultValue = 0  # Initialize resultValue

# 3. Loop through PossibleSubstringLengths:
for currentLength in range(lengthOfLine):  # From 0 to lengthOfLine - 1
    for currentIndex in range(lengthOfLine):  # From 0 to lengthOfLine - 1
        # 4. Check for Substring Reoccurrence:
        substring = inputLine[currentIndex:currentIndex + currentLength]  # Extract substring
        if substring in inputLine[currentIndex + 1:]:  # Check if the substring occurs again
            resultValue = currentLength  # Update resultValue
            break  # Exit inner loop

# 5. Output the Result:
print(resultValue)  # Output the result value
