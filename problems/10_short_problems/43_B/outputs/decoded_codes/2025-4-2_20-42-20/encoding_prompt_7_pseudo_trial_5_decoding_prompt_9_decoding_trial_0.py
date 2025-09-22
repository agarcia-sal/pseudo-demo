def checkCharacterFrequency():
    # Prompt user for the first string input
    firstString = input()
    # Prompt user for the second string input
    secondString = input()

    # Create filtered lists of characters excluding spaces
    firstFilteredList = [char for char in firstString if char != ' ']
    secondFilteredList = [char for char in secondString if char != ' ']

    # Initialize an empty list to store frequency differences
    frequencyDifferenceList = []

    # Iterate over ASCII values from 'A' (65) to 'z' (122)
    for ascii_value in range(65, 123):
        current_char = chr(ascii_value)
        # Calculate frequency difference for the current character
        frequencyDifference = firstFilteredList.count(current_char) - secondFilteredList.count(current_char)
        # Add frequency difference to the list
        frequencyDifferenceList.append(frequencyDifference)

    # Check for negative values in the frequency difference list
    if all(diff >= 0 for diff in frequencyDifferenceList):
        print("YES")
    else:
        print("NO")
