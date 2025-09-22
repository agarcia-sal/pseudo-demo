def check_character_frequency():
    # Prompt the user for the first and second strings
    string1 = input()
    string2 = input()

    # Remove spaces and create lists of characters
    s1 = [char for char in string1 if char != ' ']
    s2 = [char for char in string2 if char != ' ']

    # Initialize a list to hold frequency differences between the two strings
    frequency_differences = []

    # Loop through the ASCII values of characters from 'A' (65) to 'z' (122)
    for ascii_value in range(ord('A'), ord('z') + 1):
        char = chr(ascii_value)
        # Count occurrences in s1 and s2
        count_s1 = s1.count(char)
        count_s2 = s2.count(char)
        # Calculate the difference and add to the frequency differences list
        difference = count_s1 - count_s2
        frequency_differences.append(difference)

    # Check if there are any negative differences
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")  # Indicates that string1 has equal or more of each character compared to string2
    else:
        print("NO")   # Indicates that string2 has more of at least one character compared to string1

# Call the function to test its functionality
check_character_frequency()
