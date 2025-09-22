def check_character_frequency():
    # Prompt the user for the first string
    string1 = input()
    # Prompt the user for the second string
    string2 = input()

    # Remove spaces from both strings and create character lists
    s1 = [char for char in string1 if char != ' ']
    s2 = [char for char in string2 if char != ' ']

    # Initialize a list to hold frequency differences between the two strings
    frequency_differences = []

    # Loop through the ASCII values of characters from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        # Get the character corresponding to the ASCII value
        char = chr(ascii_value)
        
        # Count occurrences in s1 and s2
        count_in_s1 = s1.count(char)
        count_in_s2 = s2.count(char)

        # Calculate the difference and add to frequency differences list
        difference = count_in_s1 - count_in_s2
        frequency_differences.append(difference)

    # Check if there are any negative differences in frequency
    if frequency_differences.count(-1) + sum(1 for diff in frequency_differences if diff < 0) == 0:
        print("YES")  # Indicates that string1 has equal or more of each character than string2
    else:
        print("NO")  # Indicates that string2 has more of at least one character than string1

# Function invocation for testing
# You can uncomment the following line to call the function
# check_character_frequency()
