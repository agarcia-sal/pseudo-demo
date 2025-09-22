def read_input():
    # Read a line of input from the user
    return input()

def create_list_of_characters(input_string, exclude_spaces=True):
    # Strip spaces if required and convert string to list of characters
    if exclude_spaces:
        return [char for char in input_string if char != ' ']
    return list(input_string)

def count_character_in_list(characters, character_code):
    # Count occurrences of a character based on its ASCII value in the character list
    return characters.count(chr(character_code))

def main():
    # Read two lines of input, which represent two strings
    first_input = read_input()
    second_input = read_input()

    # Create two lists to hold characters from the input strings, excluding spaces
    characters_from_first_input = create_list_of_characters(first_input, exclude_spaces=True)
    characters_from_second_input = create_list_of_characters(second_input, exclude_spaces=True)

    # Initialize a list to store the frequency difference of each character
    frequency_differences = [0] * 96  # For ASCII characters A-Z and a-z

    # Calculate frequency differences for each character
    for character_code in range(65, 123):  # ASCII values for A (65) to z (122)
        frequency_in_first_input = count_character_in_list(characters_from_first_input, character_code)
        frequency_in_second_input = count_character_in_list(characters_from_second_input, character_code)
        
        # Store the frequency difference
        frequency_differences[character_code] = frequency_in_first_input - frequency_in_second_input

    # Check if all frequency differences are non-negative
    all_frequencies_non_negative = True
    for frequency in frequency_differences:
        if frequency < 0:
            all_frequencies_non_negative = False
            break  # No need to check further, we found a negative frequency

    # Output the result based on frequency check
    if all_frequencies_non_negative:
        print("YES")
    else:
        print("NO")

# Start the program
main()
