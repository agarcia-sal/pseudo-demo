def remove_spaces(input_string):
    """Removes all spaces from the input string."""
    return input_string.replace(" ", "")

def count_character_occurrences(input_string, character):
    """Counts the occurrences of a character in the input string."""
    return input_string.count(character)

def check_frequency_difference(first_input, second_input):
    """Checks if the frequency difference of characters between two strings is non-negative."""
    # Remove spaces from both inputs
    cleaned_first_input = remove_spaces(first_input)
    cleaned_second_input = remove_spaces(second_input)

    # Initialize a frequency difference list
    frequency_differences = []

    # Count occurrences for all characters from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        character = chr(character_code)
        count_in_first_input = count_character_occurrences(cleaned_first_input, character)
        count_in_second_input = count_character_occurrences(cleaned_second_input, character)
        
        # Calculate the difference in counts
        frequency_difference = count_in_first_input - count_in_second_input
        frequency_differences.append(frequency_difference)

    # Check if all frequency differences are non-negative
    non_negative_count = sum(1 for difference in frequency_differences if difference < 0)

    # Output the result based on whether any negative counts were found
    return "YES" if non_negative_count == 0 else "NO"

if __name__ == "__main__":
    # Read two strings from user input
    first_input = input()
    second_input = input()
    
    # Get the result and print it
    result = check_frequency_difference(first_input, second_input)
    print(result)
