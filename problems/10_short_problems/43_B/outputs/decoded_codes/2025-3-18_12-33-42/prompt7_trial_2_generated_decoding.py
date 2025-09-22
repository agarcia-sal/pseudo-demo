def check_character_frequency_difference():
    # Prompt the user to input two strings
    string1 = input()
    string2 = input()

    # Process the input strings to remove spaces
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")

    # Initialize a list to store frequency differences
    frequencyDifferences = []

    # Loop through the ASCII range from 'A' to 'z'
    for char_code in range(ord('A'), ord('z') + 1):
        # Get the current character
        current_char = chr(char_code)

        # Count occurrences of the current character in both strings
        countInString1 = string1.count(current_char)
        countInString2 = string2.count(current_char)

        # Calculate the difference in frequency and add to the list
        difference = countInString1 - countInString2
        frequencyDifferences.append(difference)

    # Determine if all frequencies are non-negative
    if all(diff >= 0 for diff in frequencyDifferences):
        print("YES")
    else:
        print("NO")

# Call the function to test it
check_character_frequency_difference()
