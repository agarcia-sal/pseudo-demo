# Read two input strings from the user
first_input = input()
second_input = input()

# Remove all whitespace characters from both strings
cleaned_first_string = ''.join(first_input.split())
cleaned_second_string = ''.join(second_input.split())

# Initialize a list to hold frequency differences
frequency_differences = []

# Calculate frequency of each character from 'A' (65) to 'z' (122) in ASCII
for ascii_value in range(65, 123):
    current_char = chr(ascii_value)
    frequency_difference = cleaned_first_string.count(current_char) - cleaned_second_string.count(current_char)
    frequency_differences.append(frequency_difference)

# Check if all frequency differences are non-negative
if all(diff >= 0 for diff in frequency_differences):
    print("YES")
else:
    print("NO")
