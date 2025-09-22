# Step 1: Get User Input
first_string = input()
second_string = input()

# Step 2: Remove Spaces
string1 = first_string.replace(" ", "")
string2 = second_string.replace(" ", "")

# Step 3: Count Character Frequencies
frequency_difference = []

# Loop over ASCII values from 'A' (65) to 'z' (122)
for ascii_value in range(65, 123):
    character = chr(ascii_value)  # Get the character for the current ASCII value
    count_in_first = string1.count(character)  # Count occurrences in the first string
    count_in_second = string2.count(character)  # Count occurrences in the second string
    diff = count_in_first - count_in_second  # Calculate the frequency difference
    frequency_difference.append(diff)  # Add the difference to the list

# Step 4: Check Frequency Differences
negative_count = sum(1 for diff in frequency_difference if diff < 0)  # Count how many are negative

# Step 5: Generate Output
if negative_count == 0:
    print("YES")  # The strings are anagrams
else:
    print("NO")   # The strings are not anagrams
