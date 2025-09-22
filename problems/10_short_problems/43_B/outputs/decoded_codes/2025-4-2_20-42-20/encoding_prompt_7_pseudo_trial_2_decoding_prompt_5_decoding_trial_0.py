def check_character_frequency():
    # Prompt user for the first string
    string1 = input()
    # Prompt user for the second string
    string2 = input()

    # Create lists of characters from both strings excluding spaces
    s1 = [char for char in string1 if char != ' ']
    s2 = [char for char in string2 if char != ' ']

    # Initialize a list to hold frequency differences
    frequency_differences = []

    # Loop through ASCII values from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        char = chr(ascii_value)
        # Count occurrences in s1 and s2
        count_in_s1 = s1.count(char)
        count_in_s2 = s2.count(char)
        # Calculate difference and add to the list
        difference = count_in_s1 - count_in_s2
        frequency_differences.append(difference)

    # Check for any negative differences in frequency
    if frequency_differences.count(lambda x: x < 0) == 0:
        print("YES")  # string1 has equal or more of each character
    else:
        print("NO")   # string2 has more of at least one character

# Example test case handling
# check_character_frequency() would be called to test the function functionality
