# Step 1: Read Input
String1 = input()
String2 = input()

# Step 2: Remove Spaces
CleanedString1 = [char for char in String1 if char != ' ']
CleanedString2 = [char for char in String2 if char != ' ']

# Step 3: Initialize Frequency Difference List
FrequencyDifferences = []

# Step 4: Calculate Frequency Differences
for char_code in range(ord('A'), ord('z') + 1):
    char = chr(char_code)
    count1 = CleanedString1.count(char)
    count2 = CleanedString2.count(char)
    FrequencyDifferences.append(count1 - count2)

# Step 5: Check Frequency Differences
negative_count = sum(1 for diff in FrequencyDifferences if diff < 0)

# Step 6: Output Result
if negative_count == 0:
    print("YES")
else:
    print("NO")
