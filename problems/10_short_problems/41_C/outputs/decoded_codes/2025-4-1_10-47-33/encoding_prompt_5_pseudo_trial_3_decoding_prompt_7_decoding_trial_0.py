# Start of the email formatting process

# Read input from the user
inputString = input()

# Remove leading and trailing spaces from the string
inputString = inputString.strip()

# Replace occurrences of 'dot' with '.' (representing a period)
inputString = inputString.replace('dot', '.')

# Replace occurrences of 'at' with '@' (representing an at sign)
inputString = inputString.replace('at', '@')

# If the first character is a period, prefix the string with 'dot'
if inputString.startswith('.'):
    inputString = 'dot' + inputString[1:]

# Initialize a counter and an empty list to hold processed characters
counter = 0
processedList = []

# If the first character is '@', prefix the string with 'at'
if inputString.startswith('@'):
    inputString = 'at' + inputString[1:]

# Iterate through each character in the modified input string
for character in inputString:
    # Check if the character is '@'
    if character == '@':
        # If '@' has been encountered before, append 'at' to the list
        if counter > 0:
            processedList.append('at')
            counter = 1
        else:
            # Otherwise, append '@' to the list
            processedList.append('@')
            counter = 1
    else:
        # For any other character, simply append it to the list
        processedList.append(character)

# Join the processed characters back into a single string
finalString = ''.join(processedList)

# If the last character is a period, replace it with 'dot'
if finalString.endswith('.'):
    finalString = finalString[:-1] + 'dot'

# Output the final string
print(finalString)

# End of the email formatting process
