def compare_character_frequencies():
    # Prompt user to input the first string
    first_string = input()
    # Prompt user to input the second string
    second_string = input()
    
    # Remove spaces from both input strings
    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")
    
    # Initialize a frequency list for characters from ASCII 'A' to 'z'
    frequency_list = []

    # Calculate the frequency for each character from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        # Count frequency of the current character in both cleaned strings
        frequency_first = cleaned_first_string.count(chr(character_code))
        frequency_second = cleaned_second_string.count(chr(character_code))
        
        # Calculate the difference in frequencies
        difference = frequency_first - frequency_second
        
        # Append the difference to frequency_list
        frequency_list.append(difference)

    # Evaluate the frequency differences
    negative_count = sum(1 for diff in frequency_list if diff < 0)

    # Determine the output based on the negative counts
    if negative_count == 0:
        print("YES")  # All characters in first_string are in second_string with equal or higher frequency
    else:
        print("NO")   # At least one character in first_string is missing or less frequent in second_string

# The function is wrapped in a standard way to allow for interaction
# Uncomment the following line to run the function
# compare_character_frequencies()
