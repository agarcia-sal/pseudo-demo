# Step 1: Read inputs for the two strings
first_string = input()
second_string = input()

# Step 2: Filter out spaces from the strings
filtered_first = [char for char in first_string if char != ' ']
filtered_second = [char for char in second_string if char != ' ']

# Step 3: Initialize frequency differences
frequency_differences = []

# Step 4: Calculate frequency differences for ASCII range from 'A' to 'z'
for char in range(ord('A'), ord('z') + 1):
    count_first = filtered_first.count(chr(char))
    count_second = filtered_second.count(chr(char))
    frequency_differences.append(count_first - count_second)

# Step 5: Check for negative frequencies
negative_frequencies = [freq for freq in frequency_differences if freq < 0]
negative_count = len(negative_frequencies)

# Step 6: Output result based on negative count
if negative_count == 0:
    print("YES")
else:
    print("NO")
