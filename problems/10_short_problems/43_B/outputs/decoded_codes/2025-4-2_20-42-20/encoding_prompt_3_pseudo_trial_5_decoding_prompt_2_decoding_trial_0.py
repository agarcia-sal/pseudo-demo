# Begin the program

# Step 1: Read two lines of input
firstLine = input()
secondLine = input()

# Step 2: Remove spaces from both lines
cleanedFirstLine = list(firstLine.replace(" ", ""))
cleanedSecondLine = list(secondLine.replace(" ", ""))

# Step 3: Initialize frequency difference list
frequencyDifferences = []

# Step 4: Calculate the character frequency differences
for ascii_value in range(ord('A'), ord('z') + 1):  # Iterate from 'A' to 'z'
    character = chr(ascii_value)
    countInFirstLine = cleanedFirstLine.count(character)
    countInSecondLine = cleanedSecondLine.count(character)
    difference = countInFirstLine - countInSecondLine
    frequencyDifferences.append(difference)

# Step 5: Check if all frequency differences are non-negative
hasNegativeDifference = False

for value in frequencyDifferences:
    if value < 0:
        hasNegativeDifference = True
        break  # Exit the loop if a negative difference is found

# Step 6: Print result based on the frequency differences
if not hasNegativeDifference:
    print("YES")
else:
    print("NO")

# End the program
