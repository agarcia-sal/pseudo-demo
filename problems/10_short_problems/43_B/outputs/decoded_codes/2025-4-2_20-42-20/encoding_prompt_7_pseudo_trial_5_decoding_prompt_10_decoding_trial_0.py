def check_character_frequency():
    # Prompt user for the first string input
    first_string = input()
    
    # Prompt user for the second string input
    second_string = input()
    
    # Create lists of characters excluding spaces
    first_filtered_list = [char for char in first_string if char != ' ']
    second_filtered_list = [char for char in second_string if char != ' ']
    
    # Initialize a list to store frequency differences
    frequency_difference_list = []
    
    # Calculate frequency difference for each ASCII character from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        current_char = chr(ascii_value)
        # Calculate frequency of current character in both filtered lists
        frequency_in_first = first_filtered_list.count(current_char)
        frequency_in_second = second_filtered_list.count(current_char)
        
        # Calculate the frequency difference
        frequency_difference = frequency_in_first - frequency_in_second
        
        # Add the frequency difference to the list
        frequency_difference_list.append(frequency_difference)
    
    # Check if there are any negative values in the frequency difference list
    if all(diff >= 0 for diff in frequency_difference_list):
        print("YES")
    else:
        print("NO")

# To run the function
check_character_frequency()
