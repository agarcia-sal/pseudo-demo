def check_character_frequency():
    # Prompt the user for the first string and store it in string1
    string1 = input()
    # Prompt the user for the second string and store it in string2
    string2 = input()
    
    # Create a list of characters from string1 excluding spaces
    s1 = [char for char in string1 if char != ' ']
    # Create a list of characters from string2 excluding spaces
    s2 = [char for char in string2 if char != ' ']
    
    # Initialize a list to hold frequency differences between the two strings
    frequency_differences = []
    
    # Loop through the ASCII values of characters from 'A' to 'z'
    for char in range(ord('A'), ord('z') + 1):
        # Count occurrences in s1 and s2, and calculate the difference
        count_s1 = s1.count(chr(char))
        count_s2 = s2.count(chr(char))
        difference = count_s1 - count_s2
        # Add the calculated difference to the frequency_differences list
        frequency_differences.append(difference)
    
    # Check if there are any negative differences in frequency
    if sum(difference < 0 for difference in frequency_differences) == 0:
        print("YES")  # Indicates that string1 has equal or more of each character compared to string2
    else:
        print("NO")   # Indicates that string2 has more of at least one character compared to string1

# Call the function
check_character_frequency()
