def remove_spaces(input_string):
    """Remove all spaces from the input string."""
    return ''.join(char for char in input_string if char != ' ')

def count_character(string, character_code):
    """Count occurrences of the character represented by character_code in the string."""
    char = chr(character_code)
    return string.count(char)

def count_negative(lst):
    """Count the number of elements in the list that are negative."""
    return sum(1 for x in lst if x < 0)

def main():
    # Read two input strings
    first_string = input()
    second_string = input()

    # Remove spaces from each string
    s1 = remove_spaces(first_string)
    s2 = remove_spaces(second_string)

    # Initialize a list to hold the frequency differences
    frequency_differences = []

    # Calculate frequency differences for each character from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        frequency_in_s1 = count_character(s1, character_code)
        frequency_in_s2 = count_character(s2, character_code)

        # Calculate frequency difference
        frequency_difference = frequency_in_s1 - frequency_in_s2
        frequency_differences.append(frequency_difference)

    # Check if there are any negative differences
    if count_negative(frequency_differences) == 0:
        print("YES")
    else:
        print("NO")

# Run the main function
if __name__ == "__main__":
    main()
