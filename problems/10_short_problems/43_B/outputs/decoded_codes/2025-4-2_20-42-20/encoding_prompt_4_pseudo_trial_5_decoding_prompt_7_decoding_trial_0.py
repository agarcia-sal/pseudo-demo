# Read two input strings
inputString1 = input()
inputString2 = input()

# Remove spaces from both input strings
cleanedString1 = inputString1.replace(" ", "")
cleanedString2 = inputString2.replace(" ", "")

# Initialize a frequency list to track the count difference of each character
# We consider ASCII values from 0 to 127, thus creating a list of size 128
frequencyDifference = [0] * 128

# Calculate frequency difference for each character from 'A' to 'z'
for characterCode in range(ord('A'), ord('z') + 1):
    countInString1 = cleanedString1.count(chr(characterCode))
    countInString2 = cleanedString2.count(chr(characterCode))
    frequencyDifference[characterCode] = countInString1 - countInString2

# Check if all frequency differences are non-negative
if all(count >= 0 for count in frequencyDifference):
    print("YES")
else:
    print("NO")
