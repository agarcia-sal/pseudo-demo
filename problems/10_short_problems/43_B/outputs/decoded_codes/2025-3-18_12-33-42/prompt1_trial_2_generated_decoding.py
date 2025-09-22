# Input Stage
string1 = input()
string2 = input()

# Remove spaces and create cleaned character lists
cleanedString1 = [char for char in string1 if char != ' ']
cleanedString2 = [char for char in string2 if char != ' ']

# Frequency Calculation
frequencyDifferences = []
for ascii_value in range(ord('A'), ord('z') + 1):
    char = chr(ascii_value)
    count1 = cleanedString1.count(char)
    count2 = cleanedString2.count(char)
    frequencyDifferences.append(count1 - count2)

# Output Decision
if all(diff >= 0 for diff in frequencyDifferences):
    print("YES")
else:
    print("NO")
