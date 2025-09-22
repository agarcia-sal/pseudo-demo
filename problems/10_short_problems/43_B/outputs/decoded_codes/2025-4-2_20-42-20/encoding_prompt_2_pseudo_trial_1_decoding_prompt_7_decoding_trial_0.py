# Input Reading
first_string = input()  # Read the first line of input
second_string = input()  # Read the second line of input

# String Preprocessing
cleaned_first_string = first_string.replace(" ", "")  # Remove all spaces from first_string
cleaned_second_string = second_string.replace(" ", "")  # Remove all spaces from second_string

# Frequency Calculation
character_frequencies = []  # List to hold frequency differences

# Iterate through the range of characters from 'A' to 'z'
for char in range(ord('A'), ord('z') + 1):  # Note: This includes both uppercase and lowercase characters
    char_count_first = cleaned_first_string.count(chr(char))  # Count character in cleaned_first_string
    char_count_second = cleaned_second_string.count(chr(char))  # Count character in cleaned_second_string
    frequency_difference = char_count_first - char_count_second  # Calculate the difference
    character_frequencies.append(frequency_difference)  # Append the difference to the list

# Result Evaluation
negative_count = sum(1 for freq in character_frequencies if freq < 0)  # Count negative frequency differences

# Output the result based on the count of negative values
if negative_count == 0:
    print("YES")  # All character frequencies are non-negative
else:
    print("NO")  # There are not enough characters in first_string to match second_string
