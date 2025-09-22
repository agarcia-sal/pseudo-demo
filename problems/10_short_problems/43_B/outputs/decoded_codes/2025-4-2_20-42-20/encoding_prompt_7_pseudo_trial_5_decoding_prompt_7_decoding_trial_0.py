def checkCharacterFrequency():
    # Prompt user for the first string input
    firstString = input()
    
    # Prompt user for the second string input
    secondString = input()

    # Filter the characters from both strings, excluding spaces
    firstFilteredList = [char for char in firstString if char != ' ']
    secondFilteredList = [char for char in secondString if char != ' ']

    # Initialize a list to store the frequency differences
    frequencyDifferenceList = []

    # Loop over ASCII values from 65 ('A') to 122 ('z')
    for ascii_value in range(65, 123):
        current_char = chr(ascii_value)  # Get the character from ASCII value
        # Count the occurrences of the current character in both lists
        count_first = firstFilteredList.count(current_char)
        count_second = secondFilteredList.count(current_char)
        # Calculate the frequency difference
        frequencyDifference = count_first - count_second
        # Add the frequency difference to the list
        frequencyDifferenceList.append(frequencyDifference)

    # Check if there are any negative values in the frequency difference list
    if all(diff >= 0 for diff in frequencyDifferenceList):
        print("YES")  # If no negative value, print YES
    else:
        print("NO")   # If there is a negative value, print NO

# Function can be tested by calling it
checkCharacterFrequency()
