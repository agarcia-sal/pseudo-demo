# Receive Input
firstString = input()
secondString = input()

# Process Input Strings
firstProcessed = firstString.replace(" ", "")
secondProcessed = secondString.replace(" ", "")

# Initialize Frequency List
frequencyDifference = [0] * (ord('z') - ord('A') + 1)

# Calculate Character Frequencies
for char in range(ord('A'), ord('z') + 1):
    firstCount = firstProcessed.count(chr(char))
    secondCount = secondProcessed.count(chr(char))
    frequencyDifference[char - ord('A')] = firstCount - secondCount

# Check Conditions
if all(count >= 0 for count in frequencyDifference):
    print("YES")
else:
    print("NO")
