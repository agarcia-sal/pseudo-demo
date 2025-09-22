# Input
first_string = input()
second_string = input()

# Process the Strings
filtered_first = [char for char in first_string if char != ' ']
filtered_second = [char for char in second_string if char != ' ']

# Initialize Frequency Differences
frequency_differences = []
for char in range(ord('A'), ord('z') + 1):
    count_first = filtered_first.count(chr(char))
    count_second = filtered_second.count(chr(char))
    frequency_differences.append(count_first - count_second)

# Check for Negative Frequencies
negative_frequencies = [freq for freq in frequency_differences if freq < 0]
count_negative = len(negative_frequencies)

# Output Result
if count_negative == 0:
    print("YES")
else:
    print("NO")
