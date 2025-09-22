# Function to check character frequency between two strings
def check_character_frequency():
    # Prompt the user for the first string and store it in string1
    string1 = input()
    # Prompt the user for the second string and store it in string2
    string2 = input()
    
    # Remove spaces from both strings and store the results in two new lists
    s1 = [char for char in string1 if char != " "]  # List of characters from string1 excluding spaces
    s2 = [char for char in string2 if char != " "]  # List of characters from string2 excluding spaces

    # Initialize a list to hold frequency differences between the two strings
    frequency_differences = []

    # Loop through the ASCII values of characters from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        character = chr(ascii_value)  # Get the character from ASCII value
        count_s1 = s1.count(character)  # Count occurrences in s1
        count_s2 = s2.count(character)  # Count occurrences in s2
        difference = count_s1 - count_s2  # Calculate the frequency difference
        frequency_differences.append(difference)  # Add the difference to the list

    # Check if there are any negative differences in frequency
    if frequency_differences.count(lambda x: x < 0) == 0:
        print("YES")  # All characters in string1 are at least in string2
    else:
        print("NO")   # string2 has more of at least one character than string1

# Call the function to execute it
check_character_frequency()
