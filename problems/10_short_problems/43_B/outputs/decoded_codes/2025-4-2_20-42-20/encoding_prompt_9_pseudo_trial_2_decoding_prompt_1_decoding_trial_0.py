# Step 1: Input Strings
firstString = input()
secondString = input()

# Step 2: Process Input
firstString = firstString.replace(" ", "")
secondString = secondString.replace(" ", "")

# Step 3: Initialize Frequency Count
characterDifferences = []
for char in range(ord('A'), ord('z') + 1):
    # Convert the numerical char back to a character
    character = chr(char)
    countFirst = firstString.count(character)
    countSecond = secondString.count(character)
    difference = countFirst - countSecond
    characterDifferences.append(difference)

# Step 4: Check Feasibility
negative_count = sum(1 for difference in characterDifferences if difference < 0)

# Step 5: Output the Result
if negative_count == 0:
    print("YES")
else:
    print("NO")
