# Step 1: Input
stringOne = input()
stringTwo = input()

# Step 2: Process the Strings
filteredStringOne = [char for char in stringOne if char != ' ']
filteredStringTwo = [char for char in stringTwo if char != ' ']

# Step 3: Count Character Frequencies
frequencyDifference = []
for char in range(ord('A'), ord('z') + 1):
    countOne = filteredStringOne.count(chr(char))
    countTwo = filteredStringTwo.count(chr(char))
    frequencyDifference.append(countOne - countTwo)

# Step 4: Check Frequency Conditions
negativeCounts = [count for count in frequencyDifference if count < 0]

# Step 5: Output
if not negativeCounts:
    print("YES")
else:
    print("NO")


from collections import Counter

# Step 1: Input
stringOne = input()
stringTwo = input()

# Step 2: Process the Strings
filteredStringOne = ''.join(char for char in stringOne if char != ' ')
filteredStringTwo = ''.join(char for char in stringTwo if char != ' ')

# Step 3: Count Character Frequencies
countOne = Counter(filteredStringOne)
countTwo = Counter(filteredStringTwo)

# Step 4: Check Frequency Conditions
frequencyDifference = [countOne.get(chr(char), 0) - countTwo.get(chr(char), 0) for char in range(ord('A'), ord('z') + 1)]
negativeCounts = [count for count in frequencyDifference if count < 0]

# Step 5: Output
if not negativeCounts:
    print("YES")
else:
    print("NO")
