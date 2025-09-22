def remove_spaces(input_string):
    """Remove all spaces from the input string."""
    return input_string.replace(" ", "")

def count_occurrences(input_string, character):
    """Return the number of times the character occurs in the input string."""
    return input_string.count(character)

def main():
    # Get two input strings from the user
    first_string = input()
    second_string = input()

    # Remove all spaces from the input strings
    first_string_without_spaces = remove_spaces(first_string)
    second_string_without_spaces = remove_spaces(second_string)

    # Initialize a list to hold frequency differences
    frequency_differences = []

    # Calculate frequency differences for each character from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        character = chr(character_code)
        count_in_first_string = count_occurrences(first_string_without_spaces, character)
        count_in_second_string = count_occurrences(second_string_without_spaces, character)
        difference = count_in_first_string - count_in_second_string
        frequency_differences.append(difference)

    # Check if there are any negative frequency differences
    if all(diff >= 0 for diff in frequency_differences):
        print("YES")  # Indicates first string can be made to match second string
    else:
        print("NO")  # Indicates first string cannot be made to match second string

# Calling the main function to execute the code
main()
