def checkCharacterFrequency():
    # Prompt the user for the first string
    string1 = input()
    # Prompt the user for the second string
    string2 = input()

    # Create lists s1 and s2 with characters from the input strings excluding spaces
    s1 = [char for char in string1 if char != ' ']
    s2 = [char for char in string2 if char != ' ']

    # Initialize a list to hold frequency differences between the two strings
    frequencyDifferences = []

    # Loop through the ASCII values of characters from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        # Convert ASCII value to character
        char = chr(ascii_value)
        # Count occurrences in s1 and s2
        count_s1 = s1.count(char)
        count_s2 = s2.count(char)
        # Calculate the difference
        difference = count_s1 - count_s2
        # Add the calculated difference to the frequencyDifferences list
        frequencyDifferences.append(difference)

    # Check if there are any negative differences in frequency
    if frequencyDifferences.count(lambda x: x < 0) == 0:
        print("YES")  # string1 has equal or more of each character compared to string2
    else:
        print("NO")  # string2 has more of at least one character compared to string1

# Function call - Uncomment to run
# checkCharacterFrequency()
