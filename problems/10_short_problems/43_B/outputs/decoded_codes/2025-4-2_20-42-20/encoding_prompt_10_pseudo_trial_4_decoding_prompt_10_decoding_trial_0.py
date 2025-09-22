def filter_spaces(input_string):
    """
    This function takes a string and returns a list of characters
    excluding any spaces.
    """
    return [char for char in input_string if char != ' ']

def calculate_frequency_differences(first_string, second_string):
    """
    This function calculates the frequency differences of characters
    between two input strings across the ASCII range of 'A' to 'z'.
    It returns True if there are no negative differences, otherwise False.
    """
    frequency_differences = []

    # Filter the inputs to remove spaces
    filtered_first = filter_spaces(first_string)
    filtered_second = filter_spaces(second_string)

    for character_code in range(ord('A'), ord('z') + 1):
        character = chr(character_code)
        difference = filtered_first.count(character) - filtered_second.count(character)
        frequency_differences.append(difference)

    # Check if there is any negative frequency difference
    return all(diff >= 0 for diff in frequency_differences)

def main():
    # Step 1: Collect two lines of input
    first_input = input()
    second_input = input()

    # Step 2-3: Check frequency difference
    if calculate_frequency_differences(first_input, second_input):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
