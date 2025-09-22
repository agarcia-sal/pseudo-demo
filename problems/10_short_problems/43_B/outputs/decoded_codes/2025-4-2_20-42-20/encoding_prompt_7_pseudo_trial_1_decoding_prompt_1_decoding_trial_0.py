def compareStringsForCharacterBalance():
    # INPUT: Read two strings from user
    firstString = input()
    secondString = input()
    
    # INITIALIZE: Create character lists without spaces
    firstCharacterList = [char for char in firstString if char != ' ']
    secondCharacterList = [char for char in secondString if char != ' ']

    # INITIALIZE: Create a list to store frequency differences
    frequencyDifferences = []

    # CALCULATE frequency differences for each character in the range A to z
    for characterCode in range(ord('A'), ord('z') + 1):  # ord('z') + 1 to include 'z'
        character = chr(characterCode)
        frequencyDifference = firstCharacterList.count(character) - secondCharacterList.count(character)
        frequencyDifferences.append(frequencyDifference)

    # CHECK: Determine if all frequency differences are non-negative
    if frequencyDifferences.count(-1) == 0:  # If -1 isn't part of the counts
        print("YES")
    else:
        print("NO")

# Call the function
compareStringsForCharacterBalance()
