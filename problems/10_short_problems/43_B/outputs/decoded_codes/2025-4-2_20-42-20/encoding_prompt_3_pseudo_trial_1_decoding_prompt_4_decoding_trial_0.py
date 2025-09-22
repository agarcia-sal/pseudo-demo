def remove_spaces(input_string):
    """Remove spaces from the input string."""
    return input_string.replace(" ", "")

def count_character_occurrences(input_string, character):
    """Count how many times a character appears in the input string."""
    return input_string.count(character)

def main():
    # Read two strings from user input, removing spaces
    first_input = input()
    second_input = input()

    # Remove spaces from both inputs
    cleaned_first_input = remove_spaces(first_input)
    cleaned_second_input = remove_spaces(second_input)

    # Initialize a frequency difference list to track character count differences
    frequency_differences = []

    # For each character in the range from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        character = chr(character_code)

        # Count occurrences in each cleaned input
        count_in_first_input = count_character_occurrences(cleaned_first_input, character)
        count_in_second_input = count_character_occurrences(cleaned_second_input, character)

        # Calculate the difference in counts and add to the frequency_differences list
        frequency_differences.append(count_in_first_input - count_in_second_input)

    # Check if all frequency differences are non-negative
    non_negative_count = sum(1 for diff in frequency_differences if diff < 0)

    # Output the result based on whether any negative counts were found
    if non_negative_count == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
