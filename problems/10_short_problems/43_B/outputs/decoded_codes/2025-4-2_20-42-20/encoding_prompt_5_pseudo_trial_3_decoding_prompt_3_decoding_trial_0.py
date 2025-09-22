def compare_character_frequencies():
    # Input: Get two strings from the user
    first_string = input()
    second_string = input()
    
    # Process: Remove spaces from both strings
    cleaned_strings = []
    cleaned_strings.append(first_string.replace(' ', ''))
    cleaned_strings.append(second_string.replace(' ', ''))

    # Initialize frequency differences for characters from 'A' to 'z'
    frequency_differences = []
    
    # Iterate over the ASCII values from 'A' (65) to 'z' (122)
    for char_code in range(65, 123):
        char = chr(char_code)  # Get the actual character from ASCII code
        
        # Count occurrences in the cleaned strings
        count_first = cleaned_strings[0].count(char)
        count_second = cleaned_strings[1].count(char)
        
        # Calculate the difference in counts and store it
        frequency_differences.append(count_first - count_second)

    # Check if all frequency differences are greater than or equal to zero
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")


# Function call to execute the comparison
compare_character_frequencies()
