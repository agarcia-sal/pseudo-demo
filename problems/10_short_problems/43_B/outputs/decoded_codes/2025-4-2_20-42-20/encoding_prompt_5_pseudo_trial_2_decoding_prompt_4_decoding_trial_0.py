def main():
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

def remove_spaces(input_string):
    """Remove spaces from the input string."""
    return input_string.replace(" ", "")  # Removes spaces by replacing them with an empty string.

def count_characters(string):
    """Count the occurrences of each character in the string."""
    character_count_array = [0] * 256  # Create an array of size 256 (for ASCII characters).
    for character in string:
        character_count_array[ord(character)] += 1  # Count the occurrences using ASCII values.
    return character_count_array

def calculate_frequency_differences(counts1, counts2):
    """Calculate differences in character counts for all characters."""
    differences_array = []
    for character_code in range(256):  # Loop through all possible ASCII character codes.
        difference = counts1[character_code] - counts2[character_code]
        differences_array.append(difference)  # Add the difference to the list.
    return differences_array

def all_counts_are_non_negative(differences_array):
    """Check if all counts in the differences array are non-negative."""
    for count in differences_array:
        if count < 0:  # If any count is negative, return False.
            return False
    return True  # All counts are non-negative.

if __name__ == "__main__":
    main()
