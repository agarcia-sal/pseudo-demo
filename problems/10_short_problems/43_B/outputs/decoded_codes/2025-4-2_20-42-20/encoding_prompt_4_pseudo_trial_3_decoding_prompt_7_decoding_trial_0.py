# Function to remove spaces from a string
def remove_spaces(input_string):
    # Returns a new string with all spaces removed
    return ''.join([char for char in input_string if char != ' '])

# Function to count occurrences of a character in a string
def count_character(string, character_code):
    # Convert character code to the actual character
    character = chr(character_code)
    # Count and return how many times the character appears in the string
    return string.count(character)

# Function to count how many numbers in the list are negative
def count_negative(lst):
    # Return count of negative numbers in the list
    return sum(1 for x in lst if x < 0)

# Main program
if __name__ == "__main__":
    # Read two input strings
    first_string = input()
    second_string = input()

    # Remove spaces from each string
    s1 = remove_spaces(first_string)
    s2 = remove_spaces(second_string)

    # Initialize a list to hold the frequency differences
    frequency_differences = []

    # For each character in the ASCII range from 'A' to 'z'
    for character_code in range(ord('A'), ord('z') + 1):
        # Calculate frequency of the character in s1 and s2
        frequency_in_s1 = count_character(s1, character_code)
        frequency_in_s2 = count_character(s2, character_code)

        # Calculate the difference in frequencies
        frequency_difference = frequency_in_s1 - frequency_in_s2
        # Append difference to the list
        frequency_differences.append(frequency_difference)

    # Check for negative differences in the frequency list
    if count_negative(frequency_differences) == 0:
        print("YES")
    else:
        print("NO")
