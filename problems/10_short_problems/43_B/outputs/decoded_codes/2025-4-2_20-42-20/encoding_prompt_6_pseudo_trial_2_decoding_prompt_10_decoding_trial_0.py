def read_input():
    return input()

def create_list_of_characters(input_string, exclude_spaces=True):
    if exclude_spaces:
        return [char for char in input_string if char != ' ']
    return list(input_string)

def count_character_in_list(character_list, character_code):
    return character_list.count(chr(character_code))

def main():
    # Read two lines of input, representing two strings
    first_input = read_input()
    second_input = read_input()

    # Create lists to hold characters from the input strings, excluding spaces
    characters_from_first_input = create_list_of_characters(first_input)
    characters_from_second_input = create_list_of_characters(second_input)

    # Initialize a list to store the frequency difference of each character (ASCII values 65-122)
    frequency_differences = [0] * 128  # Extend to 128 to cover all ASCII characters

    # Calculate frequency differences for each character from A (65) to z (122)
    for character_code in range(65, 123):
        frequency_in_first_input = count_character_in_list(characters_from_first_input, character_code)
        frequency_in_second_input = count_character_in_list(characters_from_second_input, character_code)
        
        # Store the frequency difference
        frequency_differences[character_code] = frequency_in_first_input - frequency_in_second_input
    
    # Check if all frequency differences are non-negative
    all_frequencies_non_negative = all(frequency >= 0 for frequency in frequency_differences[65:123])

    # Output the result based on frequency check
    if all_frequencies_non_negative:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
