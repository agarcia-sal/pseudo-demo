# Step 1: Read Input
String1 = input()
String2 = input()

# Step 2: Remove Spaces
CleanedString1 = [char for char in String1 if char != ' ']
CleanedString2 = [char for char in String2 if char != ' ']

# Step 3: Initialize Frequency Difference List
FrequencyDifferences = []

# Step 4: Calculate Frequency Differences
for code in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
    char = chr(code)
    count1 = CleanedString1.count(char)
    count2 = CleanedString2.count(char)
    frequency_difference = count1 - count2
    FrequencyDifferences.append(frequency_difference)

# Step 5: Check Frequency Differences
negative_count = sum(1 for difference in FrequencyDifferences if difference < 0)

# Step 6: Output Result
if negative_count == 0:
    print("YES")
else:
    print("NO")
