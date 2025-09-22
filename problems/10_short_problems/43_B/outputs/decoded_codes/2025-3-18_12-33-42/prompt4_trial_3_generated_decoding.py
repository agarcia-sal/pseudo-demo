def remove_spaces(input_string):
    """Remove spaces from the input string."""
    return ''.join(input_string.split())

def list_of_characters_from(input_string):
    """Convert the input string to a list of characters."""
    return list(input_string)

def count_character_in(character_list, character_code):
    """Count occurrences of a character in a list."""
    return character_list.count(chr(character_code))

def no_negative_values_in(frequency_list):
    """Check if there are any negative values in the frequency list."""
    return all(count >= 0 for count in frequency_list)

def main():
    # Read two input strings and remove spaces
    string1 = input()
    string2 = input()
    
    cleaned_string1 = remove_spaces(string1)
    cleaned_string2 = remove_spaces(string2)

    # Create lists for characters in cleaned strings
    s1 = list_of_characters_from(cleaned_string1)
    s2 = list_of_characters_from(cleaned_string2)

    # Initialize a frequency difference list
    frequency_differences = []

    # Calculate the frequency difference for each character from 'A' (65) to 'z' (122)
    for character_code in range(ord('A'), ord('z') + 1):
        count_in_string1 = count_character_in(s1, character_code)
        count_in_string2 = count_character_in(s2, character_code)
        difference = count_in_string1 - count_in_string2
        frequency_differences.append(difference)

    # Check if all frequency differences are non-negative
    if no_negative_values_in(frequency_differences):
        print("YES")  # All character counts are balanced or in favor of the first string
    else:
        print("NO")   # Some characters are more frequent in the second string

if __name__ == "__main__":
    main()
