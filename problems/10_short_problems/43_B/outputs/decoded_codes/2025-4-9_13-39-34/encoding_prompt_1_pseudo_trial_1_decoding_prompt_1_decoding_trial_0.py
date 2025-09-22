# Step 1: Get Input
firstString = input()
secondString = input()

# Step 2: Remove Spaces
cleanedFirstString = firstString.replace(" ", "")
cleanedSecondString = secondString.replace(" ", "")

# Step 3: Count Character Frequencies
differenceFrequencies = []
for ascii_value in range(65, 123):  # From 'A' (65) to 'z' (122)
    character = chr(ascii_value)  # Convert ASCII value to character
    countInFirst = cleanedFirstString.count(character)
    countInSecond = cleanedSecondString.count(character)
    differenceFrequencies.append(countInFirst - countInSecond)

# Step 4: Evaluate Character Counts
if all(diff >= 0 for diff in differenceFrequencies):  # Check if all differences are non-negative
    print("YES")
else:
    print("NO")
