# Read input strings
first_string = input()
second_string = input()

# Process the strings: filter out spaces
filtered_first = [char for char in first_string if char != ' ']
filtered_second = [char for char in second_string if char != ' ']

# Initialize frequency differences
frequency_differences = []
for char in range(ord('A'), ord('z') + 1):  # Include all ASCII characters from 'A' to 'z'
    count_first = filtered_first.count(chr(char))
    count_second = filtered_second.count(chr(char))
    frequency_differences.append(count_first - count_second)

# Check for negative frequencies
negative_frequencies = [difference for difference in frequency_differences if difference < 0]
count_negative = len(negative_frequencies)

# Output result
if count_negative == 0:
    print("YES")
else:
    print("NO")
