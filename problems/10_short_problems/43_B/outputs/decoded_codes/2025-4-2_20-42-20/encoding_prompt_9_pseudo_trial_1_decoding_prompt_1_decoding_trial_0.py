# Step 1: Retrieve Input
firstString = input()
secondString = input()

# Step 2: Preprocess Input
cleanedStrings = []
cleanedStrings.append(firstString.replace(" ", ""))
cleanedStrings.append(secondString.replace(" ", ""))
s1 = cleanedStrings[0]
s2 = cleanedStrings[1]

# Step 3: Count Character Frequencies
frequencyDifference = []
for ascii_code in range(ord('A'), ord('z') + 1):  # Adjust range to include 'z'
    character = chr(ascii_code)
    count_s1 = s1.count(character)
    count_s2 = s2.count(character)
    difference = count_s1 - count_s2
    frequencyDifference.append(difference)

# Step 4: Check Character Count Requirements
negative_count = sum(1 for diff in frequencyDifference if diff < 0)

# Step 5: Provide Output
if negative_count == 0:
    print("YES")
else:
    print("NO")
