# Retrieve Input
first_string = input()
second_string = input()

# Preprocess Input
cleaned_strings = [
    first_string.replace(" ", ""),  # Remove spaces from the first string
    second_string.replace(" ", "")   # Remove spaces from the second string
]
s1 = cleaned_strings[0]  # Cleaned first string
s2 = cleaned_strings[1]  # Cleaned second string

# Count Character Frequencies
frequency_difference = []  # To store the difference in character counts
for char in range(ord('A'), ord('z') + 1):  # ASCII range for characters
    count_in_s1 = s1.count(chr(char))  # Count in the first string
    count_in_s2 = s2.count(chr(char))  # Count in the second string
    difference = count_in_s1 - count_in_s2  # Calculate the difference
    frequency_difference.append(difference)  # Store the difference

# Check Character Count Requirements
negative_count = sum(1 for diff in frequency_difference if diff < 0)  # Count negatives

# Provide Output
if negative_count == 0:  # If there are no negative differences
    print("YES")  # Transformation is possible
else:
    print("NO")  # Transformation is not possible
