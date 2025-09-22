def checkCharacterFrequency():
    # Prompt the user for the first string
    string1 = input()
    # Prompt the user for the second string
    string2 = input()

    # Remove spaces from both strings and store the results in two new lists
    s1 = [char for char in string1 if char != ' ']
    s2 = [char for char in string2 if char != ' ']

    # Initialize a list to hold frequency differences between the two strings
    frequencyDifferences = []

    # Loop through the ASCII values of characters from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        character = chr(ascii_value)
        # Count occurrences in s1 and s2, and calculate the difference
        difference = s1.count(character) - s2.count(character)
        # Add the calculated difference to the frequencyDifferences list
        frequencyDifferences.append(difference)

    # Check if there are any negative differences in frequency
    if frequencyDifferences.count(-1) == 0 and frequencyDifferences.count(-2) == 0:
        print("YES")  # Indicates that string1 has equal or more of each character compared to string2
    else:
        print("NO")  # Indicates that string2 has more of at least one character compared to string1

# Test the function with various inputs
checkCharacterFrequency()
