# Step 1: Read two lines of input
firstLine = input()
secondLine = input()

# Step 2: Remove spaces from both lines
cleanedFirstLine = [char for char in firstLine if char != ' ']
cleanedSecondLine = [char for char in secondLine if char != ' ']

# Step 3: Initialize frequency difference list
frequencyDifferences = []

# Step 4: Calculate the character frequency differences
for ascii_value in range(ord('A'), ord('z') + 1):
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
        break

# Step 6: Print result based on the frequency differences
if not hasNegativeDifference:
    print("YES")
else:
    print("NO")


     A B C
     A B C
     

     A B
     A B C
     

     (empty line)
     (empty line)
     

     A
     A
     

     abcd
     ABCD
     

     A B C D E F G
     A B C D E F
     