# Input Reading
first_string = input()
second_string = input()

# String Preprocessing
cleaned_first_string = first_string.replace(" ", "")
cleaned_second_string = second_string.replace(" ", "")

# Frequency Calculation
character_frequencies = []
for char in range(ord('A'), ord('z') + 1):
    count_first = cleaned_first_string.count(chr(char))
    count_second = cleaned_second_string.count(chr(char))
    frequency_difference = count_first - count_second
    character_frequencies.append(frequency_difference)

# Result Evaluation
negative_count = sum(1 for freq in character_frequencies if freq < 0)
if negative_count == 0:
    print("YES")
else:
    print("NO")


from collections import Counter

def clean_string(s):
    return s.replace(" ", "")

def calculate_frequency_difference(first_cleaned, second_cleaned):
    counter_first = Counter(first_cleaned)
    counter_second = Counter(second_cleaned)
    character_differences = []
    for char in range(ord('A'), ord('z') + 1):
        diff = counter_first.get(chr(char), 0) - counter_second.get(chr(char), 0)
        character_differences.append(diff)
    return character_differences

# Input Reading
first_string = input()
second_string = input()

# String Preprocessing
cleaned_first_string = clean_string(first_string)
cleaned_second_string = clean_string(second_string)

# Frequency Calculation
frequencies = calculate_frequency_difference(cleaned_first_string, cleaned_second_string)

# Result Evaluation
if all(freq >= 0 for freq in frequencies):
    print("YES")
else:
    print("NO")
