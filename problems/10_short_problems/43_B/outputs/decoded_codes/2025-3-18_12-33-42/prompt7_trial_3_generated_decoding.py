def check_character_frequencies():
    # Step 1: Read two lines of input strings
    first_input = input()  # Read the first input string
    second_input = input()  # Read the second input string
    
    # Step 2: Remove any spaces from both strings
    cleaned_first_string = remove_spaces_from_string(first_input) 
    cleaned_second_string = remove_spaces_from_string(second_input)

    # Step 3: Calculate frequency differences for each character
    frequency_differences = []
    
    # Loop through ASCII values for 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        # Step 3a: Count occurrences of the character in both cleaned strings
        current_character = get_character_from_code(character_code)
        count_in_first_string = count_character(cleaned_first_string, current_character)
        count_in_second_string = count_character(cleaned_second_string, current_character)
        
        # Step 3b: Calculate frequency difference and add to the list
        difference = count_in_first_string - count_in_second_string
        frequency_differences.append(difference)

    # Step 4: Check if all frequencies are non-negative
    if all_values_in_list_are_non_negative(frequency_differences):
        print("YES")  # All character frequencies in first string are greater than or equal to those in second
    else:
        print("NO")   # At least one character frequency in first string is less than that in second

def remove_spaces_from_string(input_string):
    """Remove spaces from the input string and return the list of characters."""
    return [x for x in input_string if x != ' ']

def count_character(string_list, character):
    """Count occurrences of a character in a list of characters."""
    return string_list.count(character)

def all_values_in_list_are_non_negative(values_list):
    """Check if all values in the list are non-negative."""
    return all(value >= 0 for value in values_list)

def get_character_from_code(character_code):
    """Get character corresponding to the ASCII value (character_code)."""
    return chr(character_code)

def read_input():
    """Read user input string."""
    return input()

# Example of using the function
check_character_frequencies()
