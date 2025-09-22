# Step 1: Gather Input Strings
first_input = input()
second_input = input()

# Step 2: Process Strings to Remove Spaces
firstString = [char for char in first_input if char != ' ']
secondString = [char for char in second_input if char != ' ']

# Step 3: Calculate Frequency Differences
frequencyDifferences = []
for char_code in range(65, 123):  # From 'A'(65) to 'z'(122)
    char = chr(char_code)
    count_first = firstString.count(char)
    count_second = secondString.count(char)
    frequencyDifferences.append(count_first - count_second)

# Step 4: Determine Validity of Transformation
is_transformable = all(diff >= 0 for diff in frequencyDifferences)

# Step 5: Output the Result
if is_transformable:
    print("YES")
else:
    print("NO")


from collections import Counter

def can_transform(first_input, second_input):
    firstString = [char for char in first_input if char != ' ']
    secondString = [char for char in second_input if char != ' ']
    
    frequencyFirst = Counter(firstString)
    frequencySecond = Counter(secondString)
    
    for char, count in frequencySecond.items():
        if frequencyFirst[char] < count:
            return "NO"
    return "YES"

# Gather Input Strings
first_input = input()
second_input = input()

# Output the Result
result = can_transform(first_input, second_input)
print(result)
