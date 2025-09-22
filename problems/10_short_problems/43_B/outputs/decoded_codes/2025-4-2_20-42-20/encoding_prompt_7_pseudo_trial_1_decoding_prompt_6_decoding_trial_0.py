def compare_strings_for_character_balance():
    # INPUT: Read two strings from user
    first_string = input()
    second_string = input()
    
    # INITIALIZE: Create character lists without spaces
    first_character_list = [char for char in first_string if char != ' ']
    second_character_list = [char for char in second_string if char != ' ']
    
    # INITIALIZE: Create a list to store frequency differences
    frequency_differences = []
    
    # CALCULATE frequency differences for each character from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        character = chr(character_code)
        
        # Count occurrences of character in both lists
        frequency_in_first = first_character_list.count(character)
        frequency_in_second = second_character_list.count(character)
        
        # Calculate frequency difference
        frequency_difference = frequency_in_first - frequency_in_second
        frequency_differences.append(frequency_difference)
    
    # CHECK: Determine if all frequency differences are non-negative
    # If there are any negative frequencies, it indicates the second string has more of that character
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# Call the function to execute the comparison
compare_strings_for_character_balance()
