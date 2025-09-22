# Read two input strings
input_string_1 = input()
input_string_2 = input()

# Remove spaces from both input strings
cleaned_string_1 = input_string_1.replace(" ", "")
cleaned_string_2 = input_string_2.replace(" ", "")

# Initialize a frequency list to track the count difference of each character
# ASCII ranges from 0 to 127 for standard characters; using 128 for easy indexing.
frequency_difference = [0] * 128

# Calculate frequency difference for each character from 'A' to 'z'
for character_code in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
    count_in_string_1 = cleaned_string_1.count(chr(character_code))
    count_in_string_2 = cleaned_string_2.count(chr(character_code))
    frequency_difference[character_code] = count_in_string_1 - count_in_string_2

# Check if all frequency differences are non-negative
if all(count >= 0 for count in frequency_difference):
    print("YES")
else:
    print("NO")
