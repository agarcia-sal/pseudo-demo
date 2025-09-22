def check_character_frequency():
    # Prompt user for the first string input
    first_string = input()
    
    # Prompt user for the second string input
    second_string = input()

    # Create a filtered list of characters from first_string excluding spaces
    first_filtered_list = [char for char in first_string if char != ' ']
    
    # Create a filtered list of characters from second_string excluding spaces
    second_filtered_list = [char for char in second_string if char != ' ']

    # Initialize a list to hold frequency differences
    frequency_difference_list = []

    # Iterate over ASCII values from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        current_char = chr(ascii_value)
        # Calculate the frequency of the current character in both filtered lists
        first_char_count = first_filtered_list.count(current_char)
        second_char_count = second_filtered_list.count(current_char)

        # Calculate the frequency difference
        frequency_difference = first_char_count - second_char_count
        
        # Append frequency difference to the list
        frequency_difference_list.append(frequency_difference)

    # Check if there are any negative values in frequency_difference_list
    if all(diff >= 0 for diff in frequency_difference_list):
        print("YES")
    else:
        print("NO")

# Call the function to execute
check_character_frequency()
