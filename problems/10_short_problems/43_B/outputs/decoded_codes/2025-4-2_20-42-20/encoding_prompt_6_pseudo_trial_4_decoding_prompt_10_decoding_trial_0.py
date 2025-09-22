def main():
    # Read two input strings from the user
    first_input = input()
    second_input = input()
    
    # Remove spaces from both input strings and convert them to lists of characters
    first_processed_string = [char for char in first_input if char != ' ']
    second_processed_string = [char for char in second_input if char != ' ']

    # Initialize a frequency list to hold character count differences
    character_frequency_differences = [0] * 128  # Covers ASCII characters from 0 to 127

    # Calculate the differences in character frequencies between the two strings
    for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
        current_character = chr(ascii_value)
        
        # Count occurrences of current_character in both processed strings
        count_in_first_string = first_processed_string.count(current_character)
        count_in_second_string = second_processed_string.count(current_character)
        
        # Calculate frequency difference and store it
        frequency_difference = count_in_first_string - count_in_second_string
        character_frequency_differences[ascii_value] = frequency_difference

    # Count how many negative values are in character_frequency_differences
    negative_count = sum(1 for freq in character_frequency_differences if freq < 0)

    # Determine the final output based on negative counts
    if negative_count == 0:
        print("YES")  # No negative frequency differences
    else:
        print("NO")   # There are negative frequency differences

if __name__ == "__main__":
    main()
