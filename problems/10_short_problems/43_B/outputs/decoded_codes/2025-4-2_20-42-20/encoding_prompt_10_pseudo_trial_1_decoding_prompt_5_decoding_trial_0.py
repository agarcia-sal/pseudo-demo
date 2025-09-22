def main():
    # Step 1: Accept two lines of input from the user
    first_line = input()
    second_line = input()

    # Step 2: Remove spaces from both lines
    cleaned_first_line = remove_spaces(first_line)
    cleaned_second_line = remove_spaces(second_line)

    # Step 3: Initialize frequency count for characters
    frequency_counts = [0] * 58  # Array to hold frequency counts for characters from 'A' to 'z'

    # Step 4: Calculate frequency differences
    for char_value in range(ord('A'), ord('z') + 1):
        count = cleaned_first_line.count(chr(char_value))  # Count occurrences in the first line
        frequency_counts[char_value - ord('A')] = count - cleaned_second_line.count(chr(char_value))  # Calculate difference

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


# Helper Function to Remove Spaces from String
def remove_spaces(input_string):
    result = ""
    for character in input_string:
        if character != ' ':
            result += character  # Append character to result if it is not a space
    return result


# The entry point of the program
if __name__ == "__main__":
    main()
