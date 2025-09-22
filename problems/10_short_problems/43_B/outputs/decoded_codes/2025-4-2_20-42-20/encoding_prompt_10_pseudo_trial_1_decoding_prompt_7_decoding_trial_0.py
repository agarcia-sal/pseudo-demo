def remove_spaces(input_string):
    # Helper function to remove spaces from the string
    result = ""
    for character in input_string:
        if character != ' ':
            result += character  # Append non-space characters to result
    return result

def main():
    # Step 1: Accept two lines of input from the user
    first_line = input()
    second_line = input()

    # Step 2: Remove spaces from both lines
    cleaned_first_line = remove_spaces(first_line)
    cleaned_second_line = remove_spaces(second_line)

    # Step 3: Initialize frequency count for characters
    frequency_counts = [0] * 58  # Considering characters from 'A' (ASCII 65) to 'z' (ASCII 122)

    # Step 4: Calculate frequency differences
    for char_value in range(ord('A'), ord('z') + 1):
        count_first = cleaned_first_line.count(chr(char_value))  # Count occurrences in the first cleaned line
        count_second = cleaned_second_line.count(chr(char_value))  # Count occurrences in the second cleaned line
        frequency_counts[char_value - ord('A')] = count_first - count_second  # Difference in counts

    # Step 5: Check for negative frequency counts
    is_valid = True
    for count in frequency_counts:
        if count < 0:  # If any count is negative, set is_valid to False
            is_valid = False
            break  # Exit loop early if any count is negative

    # Step 6: Print result based on frequencies
    if is_valid:
        print("YES")
    else:
        print("NO")

# Run the main function
main()
