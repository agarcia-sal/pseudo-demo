# Gather Input Strings
first_input = input()
second_input = input()

# Process Strings to Remove Spaces
firstString = [char for char in first_input if char != ' ']
secondString = [char for char in second_input if char != ' ']

# Calculate Frequency Differences
frequencyDifferences = []
for char_code in range(65, 91):  # ASCII values for 'A' to 'Z'
    char = chr(char_code)
    count_first = firstString.count(char)
    count_second = secondString.count(char)
    frequencyDifferences.append(count_first - count_second)

for char_code in range(97, 123):  # ASCII values for 'a' to 'z'
    char = chr(char_code)
    count_first = firstString.count(char)
    count_second = secondString.count(char)
    frequencyDifferences.append(count_first - count_second)

# Determine Validity of Transformation
can_transform = all(diff >= 0 for diff in frequencyDifferences)

# Output the Result
if can_transform:
    print("YES")
else:
    print("NO")
