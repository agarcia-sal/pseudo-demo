# Step 1: Receive Input
first_string = input()
second_string = input()

# Step 2: Process Input
cleaned_first_string = first_string.replace(" ", "")
cleaned_second_string = second_string.replace(" ", "")

# Step 3: Initialize Frequency Count
character_frequencies = []

# Step 4: Count Character Frequencies
for char in range(ord('A'), ord('z') + 1):  # Iterate from 'A' to 'z'
    char = chr(char)  # Convert ASCII value back to character
    count_first = cleaned_first_string.count(char)
    count_second = cleaned_second_string.count(char)
    difference = count_first - count_second
    character_frequencies.append(difference)

# Step 5: Evaluate Frequencies
has_shortages = 'NO'
if any(d < 0 for d in character_frequencies):  # Check for any negative values
    has_shortages = 'YES'

# Step 6: Output Result
if has_shortages == 'NO':
    print("YES")
else:
    print("NO")
