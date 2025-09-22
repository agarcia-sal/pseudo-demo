def remove_spaces(input_string):
    """
    Helper function to remove spaces from the input string.
    
    Args:
    input_string (str): The string from which spaces will be removed.
    
    Returns:
    str: The cleaned string with no spaces.
    """
    return ''.join(char for char in input_string if char != ' ')

def main():
    # Step 1: Accept two lines of input from the user
    first_line = input()
    second_line = input()

    # Step 2: Remove spaces from both lines
    cleaned_first_line = remove_spaces(first_line)
    cleaned_second_line = remove_spaces(second_line)

    # Step 3: Initialize frequency count for characters
    frequency_counts = [0] * 58  # Initialize with length 58 for 'A' to 'z'

    # Step 4: Calculate frequency differences
    for char_value in range(ord('A'), ord('z') + 1):
        count_in_first_line = cleaned_first_line.count(chr(char_value))
        count_in_second_line = cleaned_second_line.count(chr(char_value))
        frequency_counts[char_value - ord('A')] = count_in_first_line - count_in_second_line

    # Step 5: Check for negative frequency counts
    is_valid = True
    for count in frequency_counts:
        if count < 0:
            is_valid = False
            break  # Exit loop early if any count is negative

    # Step 6: Print result based on frequencies
    if is_valid:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
