def remove_spaces(input_string):
    # Remove spaces from the input string
    return ''.join([char for char in input_string if char != ' '])

def count_character(string, character_code):
    # Count occurrences of the character represented by character_code in the string
    character = chr(character_code)  # Convert ASCII code to character
    return string.count(character)

def count_negative(lst):
    # Count how many elements in the list are less than 0
    return sum(1 for x in lst if x < 0)

# Read two input strings
first_string = input()
second_string = input()

# Remove spaces from each string and store the results in s1 and s2
s1 = remove_spaces(first_string)
s2 = remove_spaces(second_string)

# Initialize a list to hold the frequency differences between the two strings
frequency_differences = []

# For each character in the ASCII range from 'A' to 'z'
for character_code in range(ord('A'), ord('z') + 1):
    # Calculate the frequency of the character in s1 and s2
    frequency_in_s1 = count_character(s1, character_code)
    frequency_in_s2 = count_character(s2, character_code)

    # Calculate the difference in frequencies and add to the list
    frequency_difference = frequency_in_s1 - frequency_in_s2
    frequency_differences.append(frequency_difference)

# Check if there are any negative differences in the frequency list
if count_negative(frequency_differences) == 0:
    print("YES")
else:
    print("NO")
