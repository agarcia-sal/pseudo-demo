def remove_spaces(input_string):
    """Removes all spaces from the input string."""
    return input_string.replace(" ", "")

def count_characters(string):
    """Counts occurrences of each character in the string.
    
    Returns an array of size 256 (for ASCII characters) with counts of each character.
    """
    character_count_array = [0] * 256  # Initialize array for ASCII character counts
    for character in string:
        character_count_array[ord(character)] += 1  # Increment count for the ASCII value of the character
    return character_count_array

def calculate_frequency_differences(counts1, counts2):
    """Calculates the frequency differences between two character count arrays.
    
    Returns an array of differences for each ASCII character.
    """
    differences_array = []
    for character_code in range(256):  # Loop through ASCII character codes
        difference = counts1[character_code] - counts2[character_code]
        differences_array.append(difference)
    return differences_array

def all_counts_are_non_negative(differences_array):
    """Checks if all counts in the differences array are non-negative."""
    for count in differences_array:
        if count < 0:
            return False  # Found a negative count
    return True  # All counts are non-negative

def main():
    # Step 1: Receive two input strings from the user, removing any spaces
    first_input_string = remove_spaces(input())
    second_input_string = remove_spaces(input())

    # Step 2: Create two variables to hold the character counts for the input strings
    first_string_character_counts = count_characters(first_input_string)
    second_string_character_counts = count_characters(second_input_string)

    # Step 3: Compare the character counts between the two strings
    frequency_differences = calculate_frequency_differences(first_string_character_counts, second_string_character_counts)

    # Step 4: Check if all frequency differences are zero or positive
    if all_counts_are_non_negative(frequency_differences):
        print("YES")  # The first string has equal or more characters than the second
    else:
        print("NO")   # The first string does not have enough of some characters

# Only run the main function when this script is executed directly
if __name__ == "__main__":
    main()
