# Read two input strings
inputString1 = input()
inputString2 = input()

# Remove spaces from both input strings
cleanedString1 = inputString1.replace(" ", "")
cleanedString2 = inputString2.replace(" ", "")

# Initialize a frequency list to track the count difference of each character
frequencyDifference = [0] * 128  # ASCII characters from 0 to 127

# Calculate frequency difference for each character from A to z
for characterCode in range(ord('A'), ord('z') + 1):
    countInString1 = cleanedString1.count(chr(characterCode))
    countInString2 = cleanedString2.count(chr(characterCode))
    frequencyDifference[characterCode] = countInString1 - countInString2

# Check if all frequency differences are non-negative
if all(diff >= 0 for diff in frequencyDifference):
    print("YES")
else:
    print("NO")
