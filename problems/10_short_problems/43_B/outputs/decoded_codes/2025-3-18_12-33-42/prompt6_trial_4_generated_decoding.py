def main():
    # Read two input strings
    first_string = input()
    second_string = input()
    
    # Remove spaces from each string and convert them to lists of characters
    cleaned_first_string = list(first_string.replace(" ", ""))
    cleaned_second_string = list(second_string.replace(" ", ""))
    
    # Initialize a frequency difference list to track character count differences
    frequency_difference = []

    # Loop through each character code from 'A' (65) to 'z' (122)
    for character_code in range(65, 123):
        # Get the character represented by the character code
        character = chr(character_code)
        
        # Count occurrences of the character in the first cleaned string
        count_in_first_string = cleaned_first_string.count(character)
        # Count occurrences of the character in the second cleaned string
        count_in_second_string = cleaned_second_string.count(character)
        
        # Calculate the difference in counts and append to frequency_difference list
        count_difference = count_in_first_string - count_in_second_string
        frequency_difference.append(count_difference)

    # Check if there are any negative differences in the frequency_difference list
    negative_count = sum(1 for diff in frequency_difference if diff < 0)

    # Output result based on the condition
    if negative_count == 0:
        print("YES")  # If there are no negative counts, print YES
    else:
        print("NO")   # If there are negative counts, print NO

# Call the main function to execute the logic
main()
