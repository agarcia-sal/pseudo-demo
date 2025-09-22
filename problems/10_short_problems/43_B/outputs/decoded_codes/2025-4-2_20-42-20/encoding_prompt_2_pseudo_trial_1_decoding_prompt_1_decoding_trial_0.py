# Input Reading
first_string = input()
second_string = input()

# String Preprocessing
cleaned_first_string = first_string.replace(" ", "")
cleaned_second_string = second_string.replace(" ", "")

# Frequency Calculation
character_frequencies = []
for char in range(ord('A'), ord('z') + 1):
    char = chr(char)
    count_first = cleaned_first_string.count(char)
    count_second = cleaned_second_string.count(char)
    frequency_difference = count_first - count_second
    character_frequencies.append(frequency_difference)

# Result Evaluation
negative_count = sum(1 for freq in character_frequencies if freq < 0)

if negative_count == 0:
    print("YES")
else:
    print("NO")
