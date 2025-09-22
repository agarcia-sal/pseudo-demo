# Input Two Strings
firstInput = input()
secondInput = input()

# Remove Spaces from Strings
cleanFirstInput = [char for char in firstInput if char != ' ']
cleanSecondInput = [char for char in secondInput if char != ' ']

# Count Character Frequencies
frequencyDifferences = []
for ascii_value in range(65, 123):  # From 'A'(65) to 'z'(122)
    char = chr(ascii_value)
    countFirst = cleanFirstInput.count(char)
    countSecond = cleanSecondInput.count(char)
    difference = countFirst - countSecond
    frequencyDifferences.append(difference)

# Check Character Count Validity
negativeDifferences = [diff for diff in frequencyDifferences if diff < 0]
if len(negativeDifferences) == 0:
    print("YES")
else:
    print("NO")


from collections import Counter

# Input Two Strings
firstInput = input()
secondInput = input()

# Remove Spaces from Strings
cleanFirstInput = ''.join(firstInput.split())
cleanSecondInput = ''.join(secondInput.split())

# Count Character Frequencies
frequencyFirst = Counter(cleanFirstInput)
frequencySecond = Counter(cleanSecondInput)

# Check Character Count Validity
for char in frequencySecond:
    if frequencyFirst[char] < frequencySecond[char]:
        print("NO")
        break
else:
    print("YES")
