def remove_spaces(input_string):
    # Remove each space from the input string.
    return input_string.replace(" ", "")

def count_characters(string):
    # Create an array of size 256 for ASCII characters initialized with zero values.
    character_count_array = [0] * 256
    for character in string:
        # Count the occurrences of each character.
        character_count_array[ord(character)] += 1
    return character_count_array

def calculate_frequency_differences(counts1, counts2):
    # Initialize an array to hold the frequency differences.
    differences_array = []
    for character_code in range(256):
        # Calculate the difference in character counts between the two strings.
        difference = counts1[character_code] - counts2[character_code]
        differences_array.append(difference)
    return differences_array

def all_counts_are_non_negative(differences_array):
    # Check if all counts in the differences array are non-negative.
    for count in differences_array:
        if count < 0:
            return False  # Found a count that is negative.
    return True  # All counts are non-negative.

# Step 1: Receive two input strings from the user, removing any spaces.
first_input_string = remove_spaces(input())
second_input_string = remove_spaces(input())

# Step 2: Create two variables to hold the character counts for the input strings.
first_string_character_counts = count_characters(first_input_string)
second_string_character_counts = count_characters(second_input_string)

# Step 3: Compare the character counts between the two strings.
frequency_differences = calculate_frequency_differences(first_string_character_counts, second_string_character_counts)

# Step 4: Check if all frequency differences are zero or positive.
if all_counts_are_non_negative(frequency_differences):
    print("YES")  # The first string has equal or more characters than the second.
else:
    print("NO")   # The first string does not have enough of some characters.
