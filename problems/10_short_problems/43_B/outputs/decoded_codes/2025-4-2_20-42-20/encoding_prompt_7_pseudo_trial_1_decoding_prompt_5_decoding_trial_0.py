def compare_strings_for_character_balance():
    # INPUT: Read two strings from user
    first_string = input()  # Get the first string
    second_string = input()  # Get the second string
    
    # INITIALIZE: Create character lists without spaces
    first_character_list = [char for char in first_string if char != ' ']
    second_character_list = [char for char in second_string if char != ' ']

    # INITIALIZE: Create a list to store frequency differences
    frequency_differences = []

    # CALCULATE frequency differences for each character from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        char = chr(character_code)
        # Count occurrences of char in both character lists
        count_in_first = first_character_list.count(char)
        count_in_second = second_character_list.count(char)
        frequency_difference = count_in_first - count_in_second
        frequency_differences.append(frequency_difference)

    # CHECK: Determine if all frequency differences are non-negative
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# Example test cases (uncomment to test):
# compare_strings_for_character_balance() # Use inputs like "abc" and "ab" to see the output
# compare_strings_for_character_balance() # Use inputs like "abc" and "abcd" to see the output
