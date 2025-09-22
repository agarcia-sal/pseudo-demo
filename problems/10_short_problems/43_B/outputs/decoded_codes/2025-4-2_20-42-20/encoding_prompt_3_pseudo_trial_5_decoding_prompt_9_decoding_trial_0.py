# Read two lines of input
first_line = input()
second_line = input()

# Remove spaces from both lines
cleaned_first_line = [char for char in first_line if char != ' ']
cleaned_second_line = [char for char in second_line if char != ' ']

# Initialize frequency difference list
frequency_differences = []

# Calculate the character frequency differences
for ascii_value in range(ord('A'), ord('z') + 1):
    character = chr(ascii_value)
    count_in_first_line = cleaned_first_line.count(character)
    count_in_second_line = cleaned_second_line.count(character)
    difference = count_in_first_line - count_in_second_line
    frequency_differences.append(difference)

# Check if all frequency differences are non-negative
has_negative_difference = False

for value in frequency_differences:
    if value < 0:
        has_negative_difference = True
        break

# Print result based on the frequency differences
if not has_negative_difference:
    print("YES")
else:
    print("NO")
