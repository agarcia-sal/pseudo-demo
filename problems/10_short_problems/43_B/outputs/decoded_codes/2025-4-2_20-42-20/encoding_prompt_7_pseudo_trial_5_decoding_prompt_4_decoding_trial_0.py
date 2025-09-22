def check_character_frequency():
    # Prompt user for the first string input
    first_string = input()
    # Prompt user for the second string input
    second_string = input()

    # Filter out spaces and convert the strings into lists of characters
    first_filtered_list = [char for char in first_string if char != ' ']
    second_filtered_list = [char for char in second_string if char != ' ']

    # Initialize a list to store frequency differences
    frequency_difference_list = []

    # Loop through the ASCII values from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        current_char = chr(ascii_value)
        # Calculate frequency differences
        frequency_in_first = first_filtered_list.count(current_char)
        frequency_in_second = second_filtered_list.count(current_char)
        frequency_difference = frequency_in_first - frequency_in_second
        frequency_difference_list.append(frequency_difference)

    # Check if all values in frequency_difference_list are non-negative
    if all(difference >= 0 for difference in frequency_difference_list):
        print("YES")
    else:
        print("NO")

# Example call to the function (uncomment to run)
# check_character_frequency()
