# Get User Input
firstString = input()
secondString = input()

# Process Input Strings
cleanedFirstString = list(firstString.replace(" ", ""))
cleanedSecondString = list(secondString.replace(" ", ""))

# Initialize Frequency List
characterFrequency = [0] * 128  # Covers ASCII character set

# Calculate Character Frequencies for firstString
for char in cleanedFirstString:
    characterFrequency[ord(char)] += 1

# Calculate Character Frequencies for secondString
for char in cleanedSecondString:
    characterFrequency[ord(char)] -= 1

# Check Character Frequencies
canForm = True
for count in characterFrequency:
    if count < 0:
        canForm = False
        break

# Output Result
if canForm:
    print("YES")
else:
    print("NO")
