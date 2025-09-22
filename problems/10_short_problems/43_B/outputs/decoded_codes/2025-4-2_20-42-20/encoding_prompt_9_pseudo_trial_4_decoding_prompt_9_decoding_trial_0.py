# Receive Input
first_string = input()
second_string = input()

# Process Input
cleaned_first_string = first_string.replace(" ", "")
cleaned_second_string = second_string.replace(" ", "")

# Initialize Frequency Count
character_frequencies = []

# Count Character Frequencies
for char in range(ord('A'), ord('z') + 1):
    count_in_first = cleaned_first_string.count(chr(char))
    count_in_second = cleaned_second_string.count(chr(char))
    difference = count_in_first - count_in_second
    character_frequencies.append(difference)

# Evaluate Frequencies
has_shortages = 'NO'
for frequency in character_frequencies:
    if frequency < 0:  # Check for shortages
        has_shortages = 'YES'
        break

# Output Result
if has_shortages == 'NO':
    print("YES")
else:
    print("NO")
