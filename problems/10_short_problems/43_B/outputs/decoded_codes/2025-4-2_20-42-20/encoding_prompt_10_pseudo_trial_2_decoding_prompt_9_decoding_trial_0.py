def count_occurrences(target_char, character_list):
    # Helper function to count occurrences of a character in a character list
    count = 0
    for character in character_list:
        if character == target_char:
            count += 1
    return count

# Step 1: Accept input
first_string = input()
second_string = input()

# Step 2: Remove spaces from both strings
cleaned_string1 = []
cleaned_string2 = []

for character in first_string:
    if character != ' ':
        cleaned_string1.append(character)

for character in second_string:
    if character != ' ':
        cleaned_string2.append(character)

# Step 3: Calculate frequency differences of characters
frequency_differences = []

for ascii_value in range(ord('A'), ord('z') + 1):
    current_char = chr(ascii_value)
    count_in_first = count_occurrences(current_char, cleaned_string1)
    count_in_second = count_occurrences(current_char, cleaned_string2)
    frequency_differences.append(count_in_first - count_in_second)

# Step 4: Check if there are any negative frequency differences
has_negative_frequency = False
for difference in frequency_differences:
    if difference < 0:
        has_negative_frequency = True
        break

# Step 5: Output result
if not has_negative_frequency:
    print("YES")
else:
    print("NO")
