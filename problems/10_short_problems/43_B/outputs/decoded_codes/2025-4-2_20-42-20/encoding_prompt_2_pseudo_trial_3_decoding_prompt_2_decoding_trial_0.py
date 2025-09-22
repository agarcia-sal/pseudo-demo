# Input: Accept two strings of characters from the user
stringOne = input()
stringTwo = input()

# Process the Strings
filteredStringOne = [char for char in stringOne if char != ' ']
filteredStringTwo = [char for char in stringTwo if char != ' ']

# Count Character Frequencies
frequencyDifference = []
for ascii_value in range(ord('A'), ord('z') + 1):
    char = chr(ascii_value)
    countOne = filteredStringOne.count(char)
    countTwo = filteredStringTwo.count(char)
    frequencyDifference.append(countOne - countTwo)

# Check Frequency Conditions
negativeCounts = [count for count in frequencyDifference if count < 0]

# Output: Display the result
if not negativeCounts:
    print("YES")
else:
    print("NO")
