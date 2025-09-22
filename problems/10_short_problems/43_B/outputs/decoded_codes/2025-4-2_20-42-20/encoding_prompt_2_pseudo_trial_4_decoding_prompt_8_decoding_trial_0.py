# Receive Input
cleanedString1 = input().replace(" ", "")
cleanedString2 = input().replace(" ", "")

# Initialize Frequency List
frequencyDifferences = []

# Calculate Frequency Differences
for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
    char = chr(ascii_value)
    count1 = cleanedString1.count(char)
    count2 = cleanedString2.count(char)
    frequencyDifferences.append(count1 - count2)

# Check for Negative Differences
negativeDifferences = [difference for difference in frequencyDifferences if difference < 0]

if len(negativeDifferences) == 0:
    print("YES")
else:
    print("NO")


from collections import Counter

# Receive Input
cleanedString1 = input().replace(" ", "")
cleanedString2 = input().replace(" ", "")

# Count frequencies
frequency1 = Counter(cleanedString1)
frequency2 = Counter(cleanedString2)

# Check for Negative Differences
for char in frequency2:
    if frequency1[char] < frequency2[char]:
        print("NO")
        break
else:
    print("YES")
