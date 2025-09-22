def check_character_frequency():
    # Prompt the user for the first string
    string1 = input()
    # Prompt the user for the second string
    string2 = input()
    
    # Remove spaces from both strings and create lists of characters
    s1 = [char for char in string1 if char != ' ']
    s2 = [char for char in string2 if char != ' ']

    # Initialize a list to hold frequency differences
    frequency_differences = []

    # Loop through the ASCII values of characters from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        # Convert ASCII value to character
        char = chr(ascii_value)
        # Count occurrences in s1 and s2
        count_s1 = s1.count(char)
        count_s2 = s2.count(char)
        # Calculate the difference and add to the list
        difference = count_s1 - count_s2
        frequency_differences.append(difference)

    # Check for negative differences in frequency
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")  # s1 has equal or more of each character compared to s2
    else:
        print("NO")   # s2 has more of at least one character compared to s1

# Optionally you could call the function to test it
# check_character_frequency()
