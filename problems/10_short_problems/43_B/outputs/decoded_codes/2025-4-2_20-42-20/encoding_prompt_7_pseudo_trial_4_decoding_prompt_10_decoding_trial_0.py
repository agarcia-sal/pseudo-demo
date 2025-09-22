def compare_character_frequencies():
    # Read input strings from the user
    first_input_string = input()
    second_input_string = input()
    
    # Remove spaces and create a list of characters for both input strings
    first_string_characters = [char for char in first_input_string if char != ' ']
    second_string_characters = [char for char in second_input_string if char != ' ']
    
    # Initialize a list to hold frequency differences for each ASCII character
    frequency_differences = []

    # Loop through ASCII values for characters from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        # Calculate the frequency of each character and append the difference to frequency_differences
        char = chr(ascii_value)
        count_first = first_string_characters.count(char)
        count_second = second_string_characters.count(char)
        difference = count_first - count_second
        frequency_differences.append(difference)
        
    # Check if all frequency differences are non-negative
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# Call the function to execute
compare_character_frequencies()
