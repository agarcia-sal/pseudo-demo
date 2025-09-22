# Function to remove spaces from a given string
def remove_spaces(input_string):
    return input_string.replace(" ", "")

# Function to count occurrences of a character in a string
def count_occurrences(input_string, character):
    return input_string.count(character)

# Main execution block
if __name__ == "__main__":
    # Read two strings from user input
    first_input = input()
    second_input = input()

    # Remove spaces from both inputs
    cleaned_first_input = remove_spaces(first_input)
    cleaned_second_input = remove_spaces(second_input)

    # Initialize a frequency difference list to track character count differences
    frequency_differences = []

    # Iterate over characters from 'A' to 'z' based on ASCII values
    for character_code in range(ord('A'), ord('z') + 1):
        character = chr(character_code)  # Convert ASCII value to character
        
        # Count occurrences in each cleaned input
        count_in_first_input = count_occurrences(cleaned_first_input, character)
        count_in_second_input = count_occurrences(cleaned_second_input, character)
        
        # Calculate the difference in counts and add to the frequency_differences list
        frequency_differences.append(count_in_first_input - count_in_second_input)

    # Check if all frequency differences are non-negative
    non_negative_count = sum(1 for difference in frequency_differences if difference < 0)

    # Output the result based on whether any negative counts were found
    if non_negative_count == 0:
        print("YES")
    else:
        print("NO")
