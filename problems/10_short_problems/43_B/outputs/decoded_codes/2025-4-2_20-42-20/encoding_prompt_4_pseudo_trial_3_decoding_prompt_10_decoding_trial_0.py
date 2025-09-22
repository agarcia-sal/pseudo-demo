def remove_spaces(input_string):
    """
    Remove spaces from the input string.

    Parameters:
    input_string (str): The string from which to remove spaces.

    Returns:
    str: The string without spaces.
    """
    return ''.join(char for char in input_string if char != ' ')

def count_character(string, character):
    """
    Count occurrences of a character in a string.

    Parameters:
    string (str): The string to search.
    character (str): The character to count.

    Returns:
    int: The count of occurrences of the character in the string.
    """
    return string.count(character)

def count_negative(numbers):
    """
    Count how many numbers are negative in the list.

    Parameters:
    numbers (list): The list of numbers to check.

    Returns:
    int: The count of negative numbers in the list.
    """
    return sum(1 for number in numbers if number < 0)

def main():
    # Read two input strings
    first_string = input()
    second_string = input()

    # Remove spaces from each string
    s1 = remove_spaces(first_string)
    s2 = remove_spaces(second_string)

    # Initialize a list to hold the frequency differences
    frequency_differences = []

    # For each character in the ASCII range from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        character = chr(character_code)

        # Calculate the frequency of the character in s1 and s2
        frequency_in_s1 = count_character(s1, character)
        frequency_in_s2 = count_character(s2, character)

        # Calculate the difference in frequencies and add to the list
        frequency_difference = frequency_in_s1 - frequency_in_s2
        frequency_differences.append(frequency_difference)

    # Check if there are any negative differences in the frequency list
    if count_negative(frequency_differences) == 0:
        print("YES")
    else:
        print("NO")

# Run the main function
if __name__ == "__main__":
    main()
