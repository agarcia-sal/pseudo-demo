def compare_string_occurrences():
    # Get input from the user for both strings
    first_input = input()
    second_input = input()

    # Remove spaces and create lists of characters from both input strings
    first_string_characters = [char for char in first_input if char != ' ']
    second_string_characters = [char for char in second_input if char != ' ']

    # Initialize a list to store frequency differences
    frequency_differences = []

    # Loop through the ASCII values from 'A' to 'z'
    for char_code in range(ord('A'), ord('z') + 1):
        current_character = chr(char_code)

        # Count occurrences of current_character in first_string_characters
        count_in_first_input = first_string_characters.count(current_character)

        # Count occurrences of current_character in second_string_characters
        count_in_second_input = second_string_characters.count(current_character)

        # Calculate the difference in counts and add to the list
        difference = count_in_first_input - count_in_second_input
        frequency_differences.append(difference)

    # Check if there are any negative differences
    negative_count = sum(1 for diff in frequency_differences if diff < 0)

    # Output "YES" if there are no negative differences, otherwise "NO"
    if negative_count == 0:
        print("YES")
    else:
        print("NO")

# To run the function, simply call it
compare_string_occurrences()
