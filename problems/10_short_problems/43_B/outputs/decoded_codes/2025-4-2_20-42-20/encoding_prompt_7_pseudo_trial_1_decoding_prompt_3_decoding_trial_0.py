def compare_strings_for_character_balance():
    # INPUT: Read two strings from user
    first_string = input()
    second_string = input()
    
    # INITIALIZE: Create character lists without spaces
    first_character_list = [char for char in first_string if char != ' ']
    second_character_list = [char for char in second_string if char != ' ']

    # INITIALIZE: Create a list to store frequency differences
    frequency_differences = []

    # CALCULATE frequency differences for each character in the range A to z
    for character_code in range(ord('A'), ord('z') + 1):
        char = chr(character_code)
        frequency_difference = first_character_list.count(char) - second_character_list.count(char)
        frequency_differences.append(frequency_difference)

    # CHECK: Determine if all frequency differences are non-negative
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# Call the function to execute
compare_strings_for_character_balance()
