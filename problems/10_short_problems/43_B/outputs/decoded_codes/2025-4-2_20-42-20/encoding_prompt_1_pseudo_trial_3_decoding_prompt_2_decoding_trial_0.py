# Step 1: Input two strings
first_string = input()
second_string = input()

# Step 2: Process the strings to remove spaces
first_string_no_spaces = ''.join(first_string.split())
second_string_no_spaces = ''.join(second_string.split())

# Step 3: Initialize a frequency list
frequency_diff = []

# Step 4: Calculate the frequency difference
for char in range(ord('A'), ord('z') + 1):  # From 'A' to 'z'
    count_first = first_string_no_spaces.count(chr(char))
    count_second = second_string_no_spaces.count(chr(char))
    frequency_diff.append(count_first - count_second)

# Step 5: Check the frequency list for negative values
negative_count = sum(1 for value in frequency_diff if value < 0)

# Step 6: Output the result
if negative_count == 0:
    print("YES")
else:
    print("NO")
