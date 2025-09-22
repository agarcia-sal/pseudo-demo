def checkCharacterFrequency():
    # Prompt user for first string input and store it
    firstString = input()
    # Prompt user for second string input and store it
    secondString = input()

    # Filter out spaces and create lists of characters
    firstFilteredList = [char for char in firstString if char != ' ']
    secondFilteredList = [char for char in secondString if char != ' ']

    # Initialize an empty list to store frequency differences
    frequencyDifferenceList = []

    # Loop through ASCII values from 'A' (65) to 'z' (122)
    for ascii_value in range(65, 123):
        current_char = chr(ascii_value)
        # Calculate the frequency difference for the current character
        frequency_in_first = firstFilteredList.count(current_char)
        frequency_in_second = secondFilteredList.count(current_char)
        frequencyDifference = frequency_in_first - frequency_in_second
        # Add frequency difference to the list
        frequencyDifferenceList.append(frequencyDifference)

    # Check if there are no negative values in frequencyDifferenceList
    if all(diff >= 0 for diff in frequencyDifferenceList):
        print("YES")
    else:
        print("NO")

# Call the function to execute
checkCharacterFrequency()
