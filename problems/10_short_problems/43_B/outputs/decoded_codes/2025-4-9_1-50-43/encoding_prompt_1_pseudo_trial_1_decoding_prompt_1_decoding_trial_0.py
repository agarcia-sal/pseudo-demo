# 1. Receive Input Strings
firstString = input()
secondString = input()

# 2. Remove Spaces from Both Strings
cleanedFirstString = [char for char in firstString if char != ' ']
cleanedSecondString = [char for char in secondString if char != ' ']

# 3. Initialize Frequency Count
frequencyDifference = []

# 4. Calculate Character Frequencies
for char in range(ord('A'), ord('z') + 1):
    countFirst = cleanedFirstString.count(chr(char))
    countSecond = cleanedSecondString.count(chr(char))
    frequencyDifference.append(countFirst - countSecond)

# 5. Check for Sufficient Characters
missingCharacters = [diff for diff in frequencyDifference if diff < 0]
if len(missingCharacters) == 0:
    print("YES")
else:
    print("NO")
