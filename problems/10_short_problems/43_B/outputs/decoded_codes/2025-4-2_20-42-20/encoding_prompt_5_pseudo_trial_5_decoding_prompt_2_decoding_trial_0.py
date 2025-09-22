def compare_character_frequencies():
    # Receive two strings as input from the user
    first_string = input()
    second_string = input()
    
    # Remove spaces from both input strings
    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")
    
    # Initialize a frequency list for characters
    frequency_list = []
    
    # Calculate the frequency for each character from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        frequency_in_first = cleaned_first_string.count(chr(character_code))
        frequency_in_second = cleaned_second_string.count(chr(character_code))
        difference = frequency_in_first - frequency_in_second
        frequency_list.append(difference)
    
    # Evaluate the frequency differences
    negative_count = sum(1 for value in frequency_list if value < 0)

    # Determine the output based on the negative counts
    if negative_count == 0:
        print("YES")  # All characters in first_string are in second_string with equal or higher frequency
    else:
        print("NO")   # At least one character in first_string is missing or less frequent in second_string

# Call the function to execute
compare_character_frequencies()
