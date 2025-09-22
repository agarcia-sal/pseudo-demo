def readInput():
    return input()

def createListOfCharacters(inputString, excludeSpaces=True):
    return [char for char in inputString if not excludeSpaces or char != ' ']

def countCharacterInList(characterList, characterCode):
    return characterList.count(chr(characterCode))

def initializeListOfSize(size):
    return [0] * size

# Begin the main logic
firstInput = readInput()
secondInput = readInput()

# Create two lists to hold characters from the input strings, excluding spaces
charactersFromFirstInput = createListOfCharacters(firstInput, excludeSpaces=True)
charactersFromSecondInput = createListOfCharacters(secondInput, excludeSpaces=True)

# Initialize a list to store the frequency difference of each character
frequencyDifferences = initializeListOfSize(96)  # For characters A-Z and a-z

# Calculate frequency differences for each character
for characterCode in range(65, 123):  # ASCII values for A(65) to z(122)
    frequencyInFirstInput = countCharacterInList(charactersFromFirstInput, characterCode)
    frequencyInSecondInput = countCharacterInList(charactersFromSecondInput, characterCode)
    
    # Store the frequency difference
    frequencyDifferences[characterCode] = frequencyInFirstInput - frequencyInSecondInput

# Check if all frequency differences are non-negative
allFrequenciesNonNegative = True
for frequency in frequencyDifferences:
    if frequency < 0:
        allFrequenciesNonNegative = False
        break  # No need to check further, we found a negative frequency

# Output the result based on frequency check
if allFrequenciesNonNegative:
    print("YES")
else:
    print("NO")
