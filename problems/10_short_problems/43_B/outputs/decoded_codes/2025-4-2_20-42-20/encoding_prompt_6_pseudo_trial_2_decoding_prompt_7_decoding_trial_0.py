# Function to read input and return a list of characters excluding spaces
def create_list_of_characters(input_string, exclude_spaces=True):
    if exclude_spaces:
        return [char for char in input_string if char != ' ']
    return list(input_string)

# Function to count occurrences of a character based on ASCII value
def count_character_in_list(char_list, character_code):
    return char_list.count(chr(character_code))

# Main function to determine if the frequency differences are non-negative
def main():
    # Step 1: Read two lines of input
    first_input = input()
    second_input = input()

    # Step 2: Create lists of characters from both inputs
    characters_from_first_input = create_list_of_characters(first_input)
    characters_from_second_input = create_list_of_characters(second_input)

    # Step 3: Initialize a list for frequency differences
    frequency_differences = [0] * 128  # ASCII range for A-Z and a-z is 65-122

    # Step 4: Calculate frequency differences
    for character_code in range(65, 123):  # A(65) to z(122)
        frequency_in_first_input = count_character_in_list(characters_from_first_input, character_code)
        frequency_in_second_input = count_character_in_list(characters_from_second_input, character_code)
        
        # Store the frequency difference
        frequency_differences[character_code] = frequency_in_first_input - frequency_in_second_input

    # Step 5: Check if all frequency differences are non-negative
    all_frequencies_non_negative = True
    for frequency in frequency_differences:
        if frequency < 0:
            all_frequencies_non_negative = False
            break  # Found a negative frequency, no need to check further

    # Step 6: Output the result based on the frequency check
    if all_frequencies_non_negative:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    main()
