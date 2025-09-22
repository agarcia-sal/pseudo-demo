def main():
    # Read two input strings from the user
    first_input = input()
    second_input = input()
    
    # Remove spaces from both input strings and create lists of characters
    first_processed_string = [char for char in first_input if char != ' ']
    second_processed_string = [char for char in second_input if char != ' ']
    
    # Initialize a frequency list to hold character count differences
    character_frequency_differences = [0] * 256  # ASCII characters up to 255

    # Calculate the differences in character frequencies between the two strings
    for ascii_value in range(65, 123):  # ASCII from 'A' (65) to 'z' (122)
        current_character = chr(ascii_value)
        count_in_first_string = first_processed_string.count(current_character)
        count_in_second_string = second_processed_string.count(current_character)
        frequency_difference = count_in_first_string - count_in_second_string
        character_frequency_differences[ascii_value] = frequency_difference

    # Check for negative differences in the frequency
    negative_count = sum(1 for diff in character_frequency_differences if diff < 0)

    # Determine the final output based on negative counts
    if negative_count == 0:
        print("YES")  # There are no negative frequency differences
    else:
        print("NO")   # There are negative frequency differences

if __name__ == "__main__":
    main()
