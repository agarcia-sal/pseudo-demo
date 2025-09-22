# Step 1: Gather Input Strings
first_string = input()
second_string = input()

# Step 2: Process Strings to Remove Spaces
first_string_chars = [char for char in first_string if char != ' ']
second_string_chars = [char for char in second_string if char != ' ']

# Step 3: Calculate Frequency Differences
frequency_differences = []
for char_code in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
    first_count = first_string_chars.count(chr(char_code))
    second_count = second_string_chars.count(chr(char_code))
    frequency_differences.append(first_count - second_count)

# Step 4: Determine Validity of Transformation
can_transform = all(diff >= 0 for diff in frequency_differences)

# Step 5: Output the Result
if can_transform:
    print("YES")
else:
    print("NO")
