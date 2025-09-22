# Step 1: Input
first_string = input()
second_string = input()

# Step 2: Process the Strings
filtered_first = [char for char in first_string if char != ' ']
filtered_second = [char for char in second_string if char != ' ']

# Step 3: Initialize Frequency Differences
frequency_differences = [0] * (ord('z') - ord('A') + 1)  # ASCII range from A (65) to z (122)

for char in filtered_first:
    frequency_differences[ord(char) - ord('A')] += 1

for char in filtered_second:
    frequency_differences[ord(char) - ord('A')] -= 1

# Step 4: Check for Negative Frequencies
negative_frequencies = [freq for freq in frequency_differences if freq < 0]
count_negative = len(negative_frequencies)

# Step 5: Output Result
if count_negative == 0:
    print("YES")
else:
    print("NO")
