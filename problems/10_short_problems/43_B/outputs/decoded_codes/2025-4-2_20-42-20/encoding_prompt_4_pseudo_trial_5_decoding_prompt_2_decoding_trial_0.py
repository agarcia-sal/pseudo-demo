# Read two input strings
inputString1 = input()
inputString2 = input()

# Remove spaces from both input strings
cleanedString1 = inputString1.replace(" ", "")
cleanedString2 = inputString2.replace(" ", "")

# Initialize a frequency list to track the count difference of each character
# The list length is 128 to accommodate ASCII values from 0 to 127
frequencyDifference = [0] * 128

# Calculate frequency difference for each character from ASCII value of 'A' to ASCII value of 'z'
for characterCode in range(ord('A'), ord('z') + 1):
    countInString1 = cleanedString1.count(chr(characterCode))
    countInString2 = cleanedString2.count(chr(characterCode))
    frequencyDifference[characterCode] = countInString1 - countInString2

# Check if all frequency differences are non-negative
if all(x >= 0 for x in frequencyDifference):
    print("YES")
else:
    print("NO")
