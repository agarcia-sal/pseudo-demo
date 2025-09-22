# Step 1: Input Strings
firstString = input()
secondString = input()

# Step 2: Process Input
firstString = firstString.replace(" ", "")
secondString = secondString.replace(" ", "")

# Step 3: Initialize Frequency Count
characterDifferences = []

# Check frequency from 'A' to 'Z' and 'a' to 'z'
for char in range(ord('A'), ord('z') + 1):
    countFirst = firstString.count(chr(char))
    countSecond = secondString.count(chr(char))
    
    # Calculate the difference
    difference = countFirst - countSecond
    characterDifferences.append(difference)

# Step 4: Check Feasibility
negativeCount = sum(1 for difference in characterDifferences if difference < 0)

# Step 5: Output the Result
if negativeCount == 0:
    print("YES")
else:
    print("NO")
