# Step 1: Input the two strings
firstString = input()
secondString = input()

# Step 2: Remove spaces and create character lists
list1 = [char for char in firstString if char != ' ']
list2 = [char for char in secondString if char != ' ']

# Step 3: Initialize frequency difference list
frequencyDifference = []

# Step 4: Calculate frequency differences for each character A to z
for characterCode in range(ord('A'), ord('z') + 1):
    character = chr(characterCode)
    characterCountInFirst = list1.count(character)
    characterCountInSecond = list2.count(character)
    difference = characterCountInFirst - characterCountInSecond
    frequencyDifference.append(difference)

# Step 5: Check for negatives in frequency difference
negativeCount = sum(1 for diff in frequencyDifference if diff < 0)

# Step 6: Output the result
if negativeCount == 0:
    print("YES")
else:
    print("NO")
