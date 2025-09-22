# Read Input
String1 = input()
String2 = input()

# Remove Spaces
CleanedString1 = [char for char in String1 if char != ' ']
CleanedString2 = [char for char in String2 if char != ' ']

# Initialize Frequency Difference List
FrequencyDifferences = []

# Calculate Frequency Differences
for char_code in range(65, 123):  # ASCII range from 'A' (65) to 'z' (122)
    char = chr(char_code)
    count1 = CleanedString1.count(char)
    count2 = CleanedString2.count(char)
    FrequencyDifferences.append(count1 - count2)

# Check Frequency Differences
negative_count = sum(1 for diff in FrequencyDifferences if diff < 0)

# Output Result
if negative_count == 0:
    print("YES")
else:
    print("NO")
