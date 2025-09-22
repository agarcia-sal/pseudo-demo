# 1. Read Input
inputString = input().strip()  # Read a line and remove leading/trailing whitespace

# 2. Replace Keywords
inputString = inputString.replace('dot', '.')  # Replace 'dot' with '.'
inputString = inputString.replace('at', '@')    # Replace 'at' with '@'

# 3. Handle Leading Dot
if inputString and inputString[0] == '.':  # Check if the first character is a '.'
    inputString = 'dot' + inputString[1:]   # Prepend 'dot'

# 4. Initialize Counters and Containers
atCounter = 0                                 # Initialize counter for '@'
resultCharacters = []                          # Create an empty list for results

# 5. Handle Leading At Symbol
if inputString and inputString[0] == '@':    # Check if the first character is an '@'
    inputString = 'at' + inputString[1:]      # Prepend 'at'

# 6. Iterate Over Each Character
for currentCharacter in inputString:
    if currentCharacter == '@':
        if atCounter > 0:                     # Check if there is a previous '@'
            resultCharacters.append('at')      # Append 'at'
            atCounter = 1                       # Set counter to indicate repeat
        else:
            resultCharacters.append('@')        # First occurrence, just append '@'
            atCounter = 1                       # Increment counter
    else:
        resultCharacters.append(currentCharacter)  # Append any other character

# 7. Join Characters
finalString = ''.join(resultCharacters)        # Combine all characters into a single string

# 8. Handle Trailing Dot
if finalString and finalString[-1] == '.':    # Check if the last character is a '.'
    finalString = finalString[:-1] + 'dot'     # Remove the last '.', append 'dot'

# 9. Output Result
print(finalString)                             # Print the final modified string
