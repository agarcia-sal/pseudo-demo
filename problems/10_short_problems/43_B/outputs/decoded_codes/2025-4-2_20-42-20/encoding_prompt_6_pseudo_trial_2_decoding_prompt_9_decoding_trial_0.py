def create_list_of_characters(input_string):
    # Create a list of characters excluding spaces
    return [char for char in input_string if char != ' ']

def count_character_in_list(character_list, character_code):
    # Count occurrences of a given character code in the character list
    return character_list.count(chr(character_code))

# Read two lines of input, which represent two strings
first_input = input()
second_input = input()

# Create two lists to hold characters from the input strings, excluding spaces
characters_from_first_input = create_list_of_characters(first_input)
characters_from_second_input = create_list_of_characters(second_input)

# Initialize a list to store the frequency difference of each character
# For ASCII characters A-Z (65-90) and a-z (97-122)
frequency_differences = [0] * 123  # We use 123 for convenience to include up to character 122

# Calculate frequency differences for each character
for character_code in range(65, 123):  # ASCII values for A(65) to z(122)
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
