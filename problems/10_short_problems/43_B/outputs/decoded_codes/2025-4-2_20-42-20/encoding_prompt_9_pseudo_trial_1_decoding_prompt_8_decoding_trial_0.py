# Step 1: Retrieve Input
firstString = input()
secondString = input()

# Step 2: Preprocess Input
cleanedStrings = [
    firstString.replace(" ", ""), 
    secondString.replace(" ", "")
]
s1 = cleanedStrings[0]
s2 = cleanedStrings[1]

# Step 3: Count Character Frequencies
frequencyDifference = []

for char in range(ord('A'), ord('z') + 1):
    count_in_s1 = s1.count(chr(char))
    count_in_s2 = s2.count(chr(char))
    difference = count_in_s1 - count_in_s2
    frequencyDifference.append(difference)

# Step 4: Check Character Count Requirements
negative_count = sum(1 for value in frequencyDifference if value < 0)

# Step 5: Provide Output
if negative_count == 0:
    print("YES")
else:
    print("NO")


from collections import Counter

def can_transform(first_string, second_string):
    first_string = first_string.replace(" ", "")
    second_string = second_string.replace(" ", "")
    
    count_first = Counter(first_string)
    count_second = Counter(second_string)
    
    for char, count in count_second.items():
        if count_first[char] < count:
            return "NO"
    return "YES"

# Step 1: Retrieve Input
firstString = input()
secondString = input()

# Check and print output
print(can_transform(firstString, secondString))
