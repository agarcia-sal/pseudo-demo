def compare_character_frequencies():
    # Step 1: Receive two strings as input from the user
    first_string = input()
    second_string = input()
    
    # Step 2: Remove spaces from both input strings
    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")
    
    # Step 3: Initialize a frequency list for characters
    frequency_list = []
    
    # Step 4: Calculate the frequency for each character from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        char = chr(character_code)
        frequency_first = cleaned_first_string.count(char)
        frequency_second = cleaned_second_string.count(char)
        difference = frequency_first - frequency_second
        frequency_list.append(difference)
    
    # Step 5: Evaluate the frequency differences
    negative_count = sum(1 for difference in frequency_list if difference < 0)
    
    # Step 6: Determine the output based on the negative counts
    if negative_count == 0:
        print("YES")  # All characters in first_string are in second_string with equal or higher frequency
    else:
        print("NO")   # At least one character in first_string is missing or less frequent in second_string

# To run the function
compare_character_frequencies()
