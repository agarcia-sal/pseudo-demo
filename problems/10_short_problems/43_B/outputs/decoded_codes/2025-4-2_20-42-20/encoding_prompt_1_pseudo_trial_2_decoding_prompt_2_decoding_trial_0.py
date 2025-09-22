# Step 1: Input strings
first_string = input()
second_string = input()

# Step 2: Process the strings to filter out spaces
filtered_first = [char for char in first_string if char != ' ']
filtered_second = [char for char in second_string if char != ' ']

# Step 3: Initialize frequency differences
frequency_differences = []
for char in range(ord('A'), ord('z') + 1):
    char = chr(char)
    count_first = filtered_first.count(char)
    count_second = filtered_second.count(char)
    frequency_difference = count_first - count_second
    frequency_differences.append(frequency_difference)

# Step 4: Check for negative frequencies
negative_frequencies = [diff for diff in frequency_differences if diff < 0]
negative_count = len(negative_frequencies)

# Step 5: Output result
if negative_count == 0:
    print("YES")
else:
    print("NO")
