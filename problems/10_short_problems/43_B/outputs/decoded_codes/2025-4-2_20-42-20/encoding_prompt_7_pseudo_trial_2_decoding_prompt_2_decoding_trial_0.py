def check_character_frequency():
    # Prompt the user for the first string and store it in string1
    string1 = input()
    # Prompt the user for the second string and store it in string2
    string2 = input()
    
    # Remove spaces from both strings and store the results in two new lists
    s1 = [char for char in string1 if char != ' ']
    s2 = [char for char in string2 if char != ' ']
    
    # Initialize a list to hold frequency differences between the two strings
    frequency_differences = []
    
    # Loop through the ASCII values of characters from 'A' (65) to 'z' (122)
    for ascii_value in range(65, 123):
        character = chr(ascii_value)
        # Count occurrences in s1 and s2, and calculate the difference
        difference = s1.count(character) - s2.count(character)
        # Add the calculated difference to the frequency_differences list
        frequency_differences.append(difference)
    
    # Check if there are any negative differences in frequency
    if frequency_differences.count(-1) == 0 and frequency_differences.count(-2) == 0: 
        # If all characters have non-negative differences
        print("YES")  # Indicates that string1 has equal or more of each character compared to string2
    else:
        print("NO")  # Indicates that string2 has more of at least one character compared to string1

# Call the function to execute
check_character_frequency()
