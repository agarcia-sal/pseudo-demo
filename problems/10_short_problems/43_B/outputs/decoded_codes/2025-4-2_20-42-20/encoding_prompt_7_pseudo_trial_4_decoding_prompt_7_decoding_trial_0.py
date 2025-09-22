def compareCharacterFrequencies():
    # Step 1: Read input strings from the user
    firstInputString = input()
    secondInputString = input()
    
    # Step 2: Remove spaces from both input strings and create lists of characters
    firstStringCharacters = [char for char in firstInputString if char != ' ']
    secondStringCharacters = [char for char in secondInputString if char != ' ']

    # Step 3: Initialize a list to hold frequency differences for each ASCII character
    frequencyDifferences = []

    # Step 4: Loop through ASCII values for characters from 'A' to 'z'
    for x in range(ord('A'), ord('z') + 1):
        # Calculate the frequency of character and add to frequencyDifferences
        difference = firstStringCharacters.count(chr(x)) - secondStringCharacters.count(chr(x))
        frequencyDifferences.append(difference)

    # Step 5: Check if all frequency differences are non-negative
    if all(diff >= 0 for diff in frequencyDifferences):
        print("YES")
    else:
        print("NO")

# You can call the function to test it
compareCharacterFrequencies()
