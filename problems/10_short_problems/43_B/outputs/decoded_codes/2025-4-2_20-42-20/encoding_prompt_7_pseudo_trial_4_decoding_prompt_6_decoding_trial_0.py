def compare_character_frequencies():
    # Read input strings from the user
    first_input_string = input()
    second_input_string = input()
    
    # Remove spaces from both input strings and create lists of characters
    first_string_characters = list(first_input_string.replace(" ", ""))
    second_string_characters = list(second_input_string.replace(" ", ""))
    
    # Initialize a list to hold frequency differences for each ASCII character
    frequency_differences = []

    # Loop through ASCII values for characters from 'A' to 'z'
    for ascii_value in range(ord('A'), ord('z') + 1):
        # Calculate the frequency difference 
        difference = first_string_characters.count(chr(ascii_value)) - second_string_characters.count(chr(ascii_value))
        # Append the difference to frequency_differences
        frequency_differences.append(difference)

    # Check if all frequency differences are non-negative
    if all(difference >= 0 for difference in frequency_differences):
        print("YES")
    else:
        print("NO")

# Call the function to execute the comparison
compare_character_frequencies()
