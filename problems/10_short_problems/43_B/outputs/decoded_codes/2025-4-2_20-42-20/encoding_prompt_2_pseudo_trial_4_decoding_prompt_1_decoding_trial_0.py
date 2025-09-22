# Step 1: Receive Input
cleanedString1 = input().replace(" ", "")
cleanedString2 = input().replace(" ", "")

# Step 2: Initialize Frequency List
frequencyDifferences = []

# Step 3: Calculate Frequency Differences
for ascii_value in range(65, 123):  # ASCII values from 'A' (65) to 'z' (122)
    char = chr(ascii_value)
    count1 = cleanedString1.count(char)
    count2 = cleanedString2.count(char)
    frequencyDifference = count1 - count2
    frequencyDifferences.append(frequencyDifference)

# Step 4: Check for Negative Differences
negativeDifferences = [diff for diff in frequencyDifferences if diff < 0]
if not negativeDifferences:
    print("YES")
else:
    print("NO")
