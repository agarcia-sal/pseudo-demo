def main():
    # Read two strings from user input, removing spaces
    first_input = input().replace(" ", "")
    second_input = input().replace(" ", "")
    
    # Initialize a frequency difference list to track character count differences
    frequency_differences = []

    # For each character in the range from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        # Count occurrences in each cleaned input
        count_in_first_input = first_input.count(chr(character_code))
        count_in_second_input = second_input.count(chr(character_code))
        
        # Calculate the difference in counts and add to the frequency_differences list
        frequency_differences.append(count_in_first_input - count_in_second_input)

    # Check if all frequency differences are non-negative
    non_negative_count = sum(1 for diff in frequency_differences if diff < 0)

    # Output the result based on whether any negative counts were found
    if non_negative_count == 0:
        print("YES")
    else:
        print("NO")

# Run the main function
if __name__ == "__main__":
    main()
