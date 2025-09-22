# Step 1: Input two strings from the user
first_string = input()
second_string = input()

# Step 2: Process the strings to remove spaces
processed_first_string = first_string.replace(" ", "")
processed_second_string = second_string.replace(" ", "")

# Step 3: Initialize a frequency list
# This will store frequency differences for each character from 'A' to 'z'
frequency_difference = []

# Step 4: Calculate the frequency difference
# Loop through the ASCII range of characters from 'A' (65) to 'z' (122)
for char_code in range(ord('A'), ord('z') + 1):
    char = chr(char_code)  # Get the character from the ASCII code
    count_first = processed_first_string.count(char)  # Count in the first string
    count_second = processed_second_string.count(char)  # Count in the second string
    frequency_difference.append(count_first - count_second)  # Store the difference

# Step 5: Check the frequency list for negative values
negative_count = sum(1 for value in frequency_difference if value < 0)

# Step 6: Output the result
if negative_count == 0:
    print("YES")
else:
    print("NO")
