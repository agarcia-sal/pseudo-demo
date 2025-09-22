def compare_character_frequencies():
    # Prompt user for the first string and store the input
    first_string = input()
    
    # Prompt user for the second string and store the input
    second_string = input()
    
    # Remove spaces from both input strings
    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")
    
    # Initialize a frequency list to store frequency differences
    frequency_list = []
    
    # Calculate the frequency for each character from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        # Calculate frequency of character in both strings
        frequency_in_first = cleaned_first_string.count(chr(character_code))
        frequency_in_second = cleaned_second_string.count(chr(character_code))
        
        # Calculate the difference and append to frequency_list
        difference = frequency_in_first - frequency_in_second
        frequency_list.append(difference)
    
    # Count how many differences are negative (meaning not enough characters in the second string)
    negative_count = sum(1 for difference in frequency_list if difference < 0)
    
    # Determine the output based on the negative counts
    if negative_count == 0:
        print("YES")  # All characters in first_string are in second_string
    else:
        print("NO")   # At least one character in first_string is missing in second_string

# Call the function to run the program
compare_character_frequencies()
