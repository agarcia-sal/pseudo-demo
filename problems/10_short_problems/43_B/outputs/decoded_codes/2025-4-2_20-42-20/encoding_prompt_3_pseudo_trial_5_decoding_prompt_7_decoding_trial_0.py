# Step 1: Read two lines of input
firstLine = input()
secondLine = input()

# Step 2: Remove spaces from both lines and convert to lists of characters
cleanedFirstLine = list(firstLine.replace(" ", ""))
cleanedSecondLine = list(secondLine.replace(" ", ""))

# Step 3: Initialize frequency difference list
frequencyDifferences = []

# Step 4: Calculate the character frequency differences
for asciiValue in range(ord('A'), ord('z') + 1):
    character = chr(asciiValue)
    countInFirstLine = cleanedFirstLine.count(character)
    countInSecondLine = cleanedSecondLine.count(character)
    
    # Calculate the frequency difference
    difference = countInFirstLine - countInSecondLine
    frequencyDifferences.append(difference)

# Step 5: Check if all frequency differences are non-negative
hasNegativeDifference = False

for value in frequencyDifferences:
    if value < 0:  # If there is a negative difference
        hasNegativeDifference = True
        break  # No need to check further

# Step 6: Print result based on the frequency differences
if not hasNegativeDifference:
    print("YES")
else:
    print("NO")
