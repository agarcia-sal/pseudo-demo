# Step 1: Receive Input
first_string = input()
second_string = input()

# Step 2: Process Input
cleaned_first_string = first_string.replace(" ", "")
cleaned_second_string = second_string.replace(" ", "")

# Step 3: Initialize Frequency Count
character_frequencies = [0] * (ord('z') - ord('A') + 1)

# Step 4: Count Character Frequencies
for char in range(ord('A'), ord('z') + 1):
    count_first = cleaned_first_string.count(chr(char))
    count_second = cleaned_second_string.count(chr(char))
    character_frequencies[char - ord('A')] = count_first - count_second

# Step 5: Evaluate Frequencies
has_shortages = 'NO'
if any(freq < 0 for freq in character_frequencies):
    has_shortages = 'YES'

# Step 6: Output Result
if has_shortages == 'NO':
    print("YES")
else:
    print("NO")


from collections import Counter

def can_form_string():
    first_string = input()
    second_string = input()

    cleaned_first_string = first_string.replace(" ", "")
    cleaned_second_string = second_string.replace(" ", "")

    count_first = Counter(cleaned_first_string)
    count_second = Counter(cleaned_second_string)

    has_shortages = 'NO'
    for char in count_second:
        if count_second[char] > count_first.get(char, 0):
            has_shortages = 'YES'
            break

    if has_shortages == 'NO':
        print("YES")
    else:
        print("NO")
