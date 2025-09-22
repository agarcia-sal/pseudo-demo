# Step 1: Receive Input
first_string = input()
second_string = input()

# Step 2: Process Input
cleaned_first_string = first_string.replace(" ", "")
cleaned_second_string = second_string.replace(" ", "")

# Step 3: Initialize Frequency Count
character_frequencies = []

# Step 4: Count Character Frequencies
for char in range(ord('A'), ord('z') + 1):
    count_first = cleaned_first_string.count(chr(char))
    count_second = cleaned_second_string.count(chr(char))
    frequency_difference = count_first - count_second
    character_frequencies.append(frequency_difference)

# Step 5: Evaluate Frequencies
has_shortages = 'NO'
if any(count < 0 for count in character_frequencies):
    has_shortages = 'YES'

# Step 6: Output Result
if has_shortages == 'NO':
    print("YES")
else:
    print("NO")
