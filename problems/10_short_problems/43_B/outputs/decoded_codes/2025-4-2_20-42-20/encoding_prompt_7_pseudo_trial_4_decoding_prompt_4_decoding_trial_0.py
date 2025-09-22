def compare_character_frequencies():
    # Read input strings from the user
    first_input_string = input()
    second_input_string = input()
    
    # Remove spaces from both input strings and create lists of characters
    first_string_characters = [char for char in first_input_string if char != ' ']
    second_string_characters = [char for char in second_input_string if char != ' ']
    
    # Initialize a list to hold frequency differences for each ASCII character
    frequency_differences = []

    # Loop through ASCII values for characters from 'A' to 'z'
    for x in range(ord('A'), ord('z') + 1):
        char = chr(x)
        # Calculate the frequency of character and calculate the difference
        difference = first_string_characters.count(char) - second_string_characters.count(char)
        frequency_differences.append(difference)

    # Check if all frequency differences are non-negative
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")
    else:
        print("NO")

# A call to the function would be made as follows (uncomment for execution):
# compare_character_frequencies()
