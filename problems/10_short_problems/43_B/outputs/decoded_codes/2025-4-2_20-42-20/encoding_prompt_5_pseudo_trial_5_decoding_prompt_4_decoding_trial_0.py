def compare_character_frequencies():
    # Receive two strings as input from the user
    first_string = input()
    second_string = input()
    
    # Remove spaces from both input strings
    cleaned_first_string = first_string.replace(' ', '')
    cleaned_second_string = second_string.replace(' ', '')
    
    # Initialize a frequency list for characters
    frequency_list = []
    
    # Calculate the frequency for each character from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        # Get the character from its ASCII code
        char = chr(character_code)
        
        # Count the occurrences in both cleaned strings
        frequency_in_first_string = cleaned_first_string.count(char)
        frequency_in_second_string = cleaned_second_string.count(char)
        
        # Calculate the difference and append to the frequency list
        difference = frequency_in_first_string - frequency_in_second_string
        frequency_list.append(difference)
    
    # Evaluate the frequency differences
    negative_count = sum(1 for value in frequency_list if value < 0)
    
    # Determine the output based on the negative counts
    if negative_count == 0:
        print("YES")  # All characters in first_string are present in second_string
    else:
        print("NO")   # At least one character in first_string is missing or less frequent in second_string

# Calling the function to execute
compare_character_frequencies()
