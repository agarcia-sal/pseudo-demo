def read_input():
    return input()

def create_list_of_characters(s, exclude_spaces=True):
    if exclude_spaces:
        return [char for char in s if char != ' ']
    return list(s)

def count_character_in_list(characters_list, character_code):
    return characters_list.count(chr(character_code))

# BEGIN
# Read two lines of input, which represent two strings
first_input = read_input()
second_input = read_input()

# Create two lists to hold characters from the input strings, excluding spaces
characters_from_first_input = create_list_of_characters(first_input, exclude_spaces=True)
characters_from_second_input = create_list_of_characters(second_input, exclude_spaces=True)

# Initialize a list to store the frequency difference of each character
frequency_differences = [0] * 96  # For characters A-Z and a-z

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
# END
