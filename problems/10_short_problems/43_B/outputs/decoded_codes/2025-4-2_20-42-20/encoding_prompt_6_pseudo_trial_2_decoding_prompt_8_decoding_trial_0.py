def readInput():
    return input()

def createListOfCharacters(string, excludeSpaces):
    if excludeSpaces:
        return [char for char in string if char != ' ']
    return list(string)

def countCharacterInList(characters, characterCode):
    return characters.count(chr(characterCode))

def main():
    # Read two lines of input
    firstInput = readInput()
    secondInput = readInput()

    # Create character lists, excluding spaces
    charactersFromFirstInput = createListOfCharacters(firstInput, excludeSpaces=True)
    charactersFromSecondInput = createListOfCharacters(secondInput, excludeSpaces=True)

    # Initialize frequency differences list
    frequencyDifferences = [0] * 96  # For ASCII values A-Z and a-z

    # Calculate frequency differences
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
            break  # No need to check further

    # Output the result
    if allFrequenciesNonNegative:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
