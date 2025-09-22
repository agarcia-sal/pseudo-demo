# Initialize Variables
firstInput = []
secondInput = []

# Get Input from User
firstInput = list(input().replace(" ", ""))
secondInput = list(input().replace(" ", ""))

# Count Characters Frequency
characterFrequencyDifference = []

for char_code in range(65, 123):  # ASCII values from 'A' to 'z'
    char = chr(char_code)
    count_first = firstInput.count(char)
    count_second = secondInput.count(char)
    difference = count_first - count_second
    characterFrequencyDifference.append(difference)

# Evaluate Results
negative_count = sum(1 for difference in characterFrequencyDifference if difference < 0)

if negative_count == 0:
    print("YES")
else:
    print("NO")
