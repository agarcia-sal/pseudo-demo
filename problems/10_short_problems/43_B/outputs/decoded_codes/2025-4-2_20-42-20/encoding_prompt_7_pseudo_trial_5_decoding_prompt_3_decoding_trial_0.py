def check_character_frequency():
    # Prompt user for the first string input
    first_string = input()
    
    # Prompt user for the second string input
    second_string = input()
    
    # Filter out spaces from the input strings
    first_filtered_list = [char for char in first_string if char != ' ']
    second_filtered_list = [char for char in second_string if char != ' ']
    
    # Initialize a list to store frequency differences
    frequency_difference_list = []
    
    # Loop through ASCII values from 'A' (65) to 'z' (122)
    for ascii_value in range(ord('A'), ord('z') + 1):
        current_char = chr(ascii_value)  # Convert ASCII value to character
        
        # Calculate frequency difference
        frequency_in_first = first_filtered_list.count(current_char)
        frequency_in_second = second_filtered_list.count(current_char)
        frequency_difference = frequency_in_first - frequency_in_second
        
        # Add the frequency difference to the list
        frequency_difference_list.append(frequency_difference)
    
    # Check for negative values in frequency_difference_list
    if all(value >= 0 for value in frequency_difference_list):
        print("YES")
    else:
        print("NO")
