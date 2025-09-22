# Retrieve Input
firstString = input()
secondString = input()

# Preprocess Input
cleanedStrings = [
    firstString.replace(" ", ""),
    secondString.replace(" ", "")
]
s1 = cleanedStrings[0]  # Cleaned version of firstString
s2 = cleanedStrings[1]  # Cleaned version of secondString

# Count Character Frequencies
frequencyDifference = []
for char in range(ord('A'), ord('z') + 1):  # Iterate over ASCII values from 'A' to 'z'
    count_s1 = s1.count(chr(char))  # Count occurrences of char in s1
    count_s2 = s2.count(chr(char))  # Count occurrences of char in s2
    difference = count_s1 - count_s2  # Calculate the difference
    frequencyDifference.append(difference)  # Append the difference to the list

# Check Character Count Requirements
insufficient_count = sum(1 for diff in frequencyDifference if diff < 0)

# Provide Output
if insufficient_count == 0:
    print("YES")  # Transformation is possible
else:
    print("NO")   # Transformation is not possible
