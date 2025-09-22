# Step 1: Read input
first_string = input()
second_string = input()

# Step 2: Remove spaces from both strings
filtered_first_string = []
filtered_second_string = []

for character in first_string:
    if character != ' ':
        filtered_first_string.append(character)

for character in second_string:
    if character != ' ':
        filtered_second_string.append(character)

# Step 3: Count character frequency differences
frequency_differences = []

for character_code in range(ord('A'), ord('z') + 1):
    character = chr(character_code)
    count_in_first_string = filtered_first_string.count(character)
    count_in_second_string = filtered_second_string.count(character)
    difference = count_in_first_string - count_in_second_string
    frequency_differences.append(difference)

# Step 4: Check if any frequency difference is negative
has_negative_difference = False

for difference in frequency_differences:
    if difference < 0:
        has_negative_difference = True
        break

# Step 5: Output the result
if not has_negative_difference:
    print("YES")
else:
    print("NO")
