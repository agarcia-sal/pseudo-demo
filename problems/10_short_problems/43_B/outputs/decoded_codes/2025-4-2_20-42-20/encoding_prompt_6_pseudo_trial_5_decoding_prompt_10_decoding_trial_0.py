def read_input():
    """Reads two strings from user input."""
    first_string = input()
    second_string = input()
    return first_string, second_string


def remove_spaces(s):
    """Removes spaces from the given string."""
    return s.replace(" ", "")


def calculate_character_frequencies(first_string, second_string):
    """Calculates frequency differences of characters between two strings."""
    character_frequency = [0] * 128  # ASCII characters

    for char in range(65, 123):  # A-Z (65-90) and a-z (97-122)
        # Convert int back to char for counting
        char = chr(char)
        count_in_first_string = first_string.count(char)
        count_in_second_string = second_string.count(char)

        # Calculate the difference and store it
        character_frequency[ord(char)] = count_in_first_string - count_in_second_string

    return character_frequency


def check_validity(character_frequency):
    """Checks if all frequency differences are non-negative."""
    for count in character_frequency:
        if count < 0:
            return False
    return True


def main():
    """Main function to execute the logic."""
    # Step 1: Read two strings from user input
    first_string, second_string = read_input()

    # Step 2: Remove spaces from both strings
    first_string = remove_spaces(first_string)
    second_string = remove_spaces(second_string)

    # Step 4: Calculate character frequencies
    character_frequency = calculate_character_frequencies(first_string, second_string)

    # Step 5: Check validity of character frequency differences
    is_valid = check_validity(character_frequency)

    # Step 6: Output result based on validity check
    if is_valid:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
