# Step 1: Input
stringOne = input()
stringTwo = input()

# Step 2: Process the Strings
filteredStringOne = [char for char in stringOne if char != ' ']
filteredStringTwo = [char for char in stringTwo if char != ' ']

# Step 3: Count Character Frequencies
frequencyDifference = []
for ascii_value in range(ord('A'), ord('z') + 1):
    char = chr(ascii_value)
    countOne = filteredStringOne.count(char)
    countTwo = filteredStringTwo.count(char)
    difference = countOne - countTwo
    frequencyDifference.append(difference)

# Step 4: Check Frequency Conditions
negativeCounts = [count for count in frequencyDifference if count < 0]
if not negativeCounts:
    # Step 5: Output
    print("YES")
else:
    # Step 5: Output
    print("NO")
