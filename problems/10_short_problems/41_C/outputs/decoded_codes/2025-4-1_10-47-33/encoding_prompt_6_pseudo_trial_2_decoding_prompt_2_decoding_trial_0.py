# Read a line of input and remove any leading/trailing whitespace
InputString = input().strip()

# Replace 'dot' with '.' and 'at' with '@' in the input string
InputString = InputString.replace('dot', '.')
InputString = InputString.replace('at', '@')

# If the first character is '.', prepend 'dot' to the string
if InputString and InputString[0] == '.':
    InputString = 'dot' + InputString[1:]

# Initialize a counter for occurrences of '@' and an empty list to hold the result
AtSymbolCounter = 0
ResultList = []

# If the first character is '@', prepend 'at' to the string
if InputString and InputString[0] == '@':
    InputString = 'at' + InputString[1:]

# Iterate through each character in the modified input string
for EachCharacter in InputString:
    if EachCharacter == '@':
        # If another '@' has already been processed
        if AtSymbolCounter > 0:
            # Append 'at' to the result list
            ResultList.append('at')
            # Update the counter
            AtSymbolCounter = 1
        else:
            # Append '@' to the result list
            ResultList.append('@')
            # Update the counter
            AtSymbolCounter = 1
    else:
        # Append the current character to the result list
        ResultList.append(EachCharacter)

# Join the list into a single string
ResultString = ''.join(ResultList)

# If the last character is '.', replace it with 'dot'
if ResultString and ResultString[-1] == '.':
    ResultString = ResultString[:-1] + 'dot'

# Print the final result string
print(ResultString)
