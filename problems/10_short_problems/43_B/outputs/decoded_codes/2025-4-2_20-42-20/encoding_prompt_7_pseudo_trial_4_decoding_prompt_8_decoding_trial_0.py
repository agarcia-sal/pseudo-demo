def compareCharacterFrequencies():
    # Read input strings from the user
    firstInputString = input()
    secondInputString = input()
    
    # Remove spaces from both input strings and store the results
    firstStringCharacters = [char for char in firstInputString if char != ' ']
    secondStringCharacters = [char for char in secondInputString if char != ' ']
    
    # Initialize a list to hold frequency differences for each ASCII character
    frequencyDifferences = []

    # Loop through ASCII values for characters from 'A' to 'z'
    for x in range(ord('A'), ord('z') + 1):
        difference = firstStringCharacters.count(chr(x)) - secondStringCharacters.count(chr(x))
        frequencyDifferences.append(difference)

    # Check if all frequency differences are non-negative
    if all(diff >= 0 for diff in frequencyDifferences):
        print("YES")
    else:
        print("NO")

# Example of usage
compareCharacterFrequencies()
