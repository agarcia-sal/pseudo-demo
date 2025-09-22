# Step 1: Get user input
string1 = input()
string2 = input()

# Step 2: Clean the input strings by removing spaces
clean_string1 = string1.replace(" ", "")
clean_string2 = string2.replace(" ", "")

# Step 3: Initialize a dictionary to hold frequency differences
frequency_differences = {}

# Step 4: Calculate the frequency of each character (from 'A' to 'z')
for character in range(ord('A'), ord('z') + 1):
    char = chr(character)
    count_in_string1 = clean_string1.count(char)
    count_in_string2 = clean_string2.count(char)
    frequency_differences[char] = count_in_string1 - count_in_string2

# Step 5: Check if all frequency differences are non-negative
negative_frequency_count = 0

for difference in frequency_differences.values():
    if difference < 0:
        negative_frequency_count += 1

# Step 6: Output the result based on frequency check
if negative_frequency_count == 0:
    print("YES")
else:
    print("NO")
