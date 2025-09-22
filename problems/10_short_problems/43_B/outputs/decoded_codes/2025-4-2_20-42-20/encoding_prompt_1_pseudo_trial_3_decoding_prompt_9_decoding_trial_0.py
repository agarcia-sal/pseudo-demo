# Input two strings from the user
first_string = input()
second_string = input()

# Process the strings to remove spaces
first_string_no_spaces = ''.join(char for char in first_string if char != ' ')
second_string_no_spaces = ''.join(char for char in second_string if char != ' ')

# Initialize a frequency list for characters from 'A' to 'z'
frequency_difference = []

# Calculate the frequency difference for each character
for char in range(ord('A'), ord('z') + 1):
    count_first = first_string_no_spaces.count(chr(char))
    count_second = second_string_no_spaces.count(chr(char))
    difference = count_first - count_second
    frequency_difference.append(difference)

# Check the frequency list for negative values
negative_count = sum(1 for value in frequency_difference if value < 0)

# Output the result based on the presence of negative values
if negative_count == 0:
    print("YES")
else:
    print("NO")
