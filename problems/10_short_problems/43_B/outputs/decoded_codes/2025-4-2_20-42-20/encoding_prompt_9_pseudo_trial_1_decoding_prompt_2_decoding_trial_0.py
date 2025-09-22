# Step 1: Retrieve Input
firstString = input()
secondString = input()

# Step 2: Preprocess Input
cleanedStrings = [
    firstString.replace(" ", ""),  # Remove spaces from firstString
    secondString.replace(" ", "")   # Remove spaces from secondString
]
s1 = cleanedStrings[0]  # Store cleaned version of firstString
s2 = cleanedStrings[1]  # Store cleaned version of secondString

# Step 3: Count Character Frequencies
frequencyDifference = []  # List to store frequency differences

for char in range(ord('A'), ord('z') + 1):  # Loop through ASCII values from 'A' to 'z'
    count_s1 = s1.count(chr(char))  # Count occurrences of char in s1
    count_s2 = s2.count(chr(char))  # Count occurrences of char in s2
    difference = count_s1 - count_s2  # Calculate the difference
    frequencyDifference.append(difference)  # Add difference to the list

# Step 4: Check Character Count Requirements
negative_count = sum(1 for diff in frequencyDifference if diff < 0)  # Count negative differences

# Step 5: Provide Output
if negative_count == 0:  # If no negative differences
    print("YES")  # Transformation possible
else:
    print("NO")  # Transformation not possible
