def remove_spaces(input_string):
    return input_string.replace(" ", "")

def count_characters(string):
    character_count_array = [0] * 256  # For ASCII characters
    for character in string:
        character_count_array[ord(character)] += 1  # Increment count for the character
    return character_count_array

def calculate_frequency_differences(counts1, counts2):
    differences_array = []
    for character_code in range(256):
        difference = counts1[character_code] - counts2[character_code]
        differences_array.append(difference)
    return differences_array

def all_counts_are_non_negative(differences_array):
    for count in differences_array:
        if count < 0:
            return False  # Found a count that is negative.
    return True  # All counts are non-negative.

# Main execution flow
first_input_string = remove_spaces(input())
second_input_string = remove_spaces(input())

first_string_character_counts = count_characters(first_input_string)
second_string_character_counts = count_characters(second_input_string)

frequency_differences = calculate_frequency_differences(first_string_character_counts, second_string_character_counts)

if all_counts_are_non_negative(frequency_differences):
    print("YES")  # The first string has equal or more characters than the second.
else:
    print("NO")   # The first string does not have enough of some characters.
