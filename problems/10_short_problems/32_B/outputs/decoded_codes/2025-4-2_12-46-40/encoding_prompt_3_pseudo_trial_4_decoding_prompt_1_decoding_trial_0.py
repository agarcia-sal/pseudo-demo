# BEGIN PROGRAM

# Read input string from standard input
stringInput = input()  # Getting input from the user
stringInput = stringInput.strip()  # Removing leading and trailing whitespace

# Initialize variables
currentIndex = 0
resultString = ""  # Empty string to store the result

# Process the input string
while currentIndex < len(stringInput):  # While currentIndex is less than the length of stringInput
    if stringInput[currentIndex] == '.':  # If character at currentIndex is '.'
        # Append '0' for a single dot
        resultString += '0'  # Append '0' to resultString
        currentIndex += 1  # Increment currentIndex by 1
    elif (currentIndex + 1 < len(stringInput) and 
          stringInput[currentIndex + 1] == '.'):  # If character plus one is '.'
        # Append '1' for two consecutive dots (dot followed by a dot)
        resultString += '1'  # Append '1' to resultString
        currentIndex += 2  # Increment currentIndex by 2
    else:  # For any other two characters
        # Append '2' for any other two characters (dot followed by a different character)
        resultString += '2'  # Append '2' to resultString
        currentIndex += 2  # Increment currentIndex by 2

# Output the result
print(resultString)  # Print the resultString

# END PROGRAM
