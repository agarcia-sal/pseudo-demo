def remove_spaces(input_string):
    # Remove spaces from the input string
    return ''.join([char for char in input_string if char != ' '])

def count_character(string, character_code):
    # Count occurrences of the character represented by character_code in the string
    return string.count(chr(character_code))

def count_negative(lst):
    # Count elements in the list that are less than 0
    return sum(1 for item in lst if item < 0)

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
    # Calculate the frequency of the character in s1 and s2
    frequency_in_s1 = count_character(s1, character_code)
    frequency_in_s2 = count_character(s2, character_code)

    # Calculate the difference in frequencies
    frequency_difference = frequency_in_s1 - frequency_in_s2
    frequency_differences.append(frequency_difference)

# Check for negative differences in the frequency list
if count_negative(frequency_differences) == 0:
    print("YES")
else:
    print("NO")
