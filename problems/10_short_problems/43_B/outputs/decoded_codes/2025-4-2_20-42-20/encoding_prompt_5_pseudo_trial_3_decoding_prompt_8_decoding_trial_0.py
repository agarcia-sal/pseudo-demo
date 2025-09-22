def CompareCharacterFrequencies():
    # Get the first string from the user and remove spaces
    first_string = input().replace(" ", "")
    # Get the second string from the user and remove spaces
    second_string = input().replace(" ", "")

    # Initialize a list to hold the differences in character frequencies
    frequencyDifferences = []

    # Loop through ASCII values from 'A' to 'z'
    for char_code in range(ord('A'), ord('z') + 1):
        # Count occurrences of the character in both strings
        count_in_first = first_string.count(chr(char_code))
        count_in_second = second_string.count(chr(char_code))
        
        # Calculate the difference and append it to the list
        frequencyDifferences.append(count_in_first - count_in_second)

    # Check for negative differences
    if all(diff >= 0 for diff in frequencyDifferences):
        print("YES")
    else:
        print("NO")

# This function can be tested by calling it directly
