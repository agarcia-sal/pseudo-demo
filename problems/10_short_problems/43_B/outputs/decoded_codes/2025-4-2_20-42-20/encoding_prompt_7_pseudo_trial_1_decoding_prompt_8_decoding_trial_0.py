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
    for characterCode in range(ord('A'), ord('z') + 1):
        frequencyDifference = firstCharacterList.count(chr(characterCode)) - secondCharacterList.count(chr(characterCode))
        frequencyDifferences.append(frequencyDifference)

    # CHECK: Determine if all frequency differences are non-negative
    if all(diff >= 0 for diff in frequencyDifferences):
        print("YES")
    else:
        print("NO")


     hello
     hello
     

     abc
     xyz
     

     abc
     abcd
     

     aAa
     Aaa
     

     a b c
     a b
     