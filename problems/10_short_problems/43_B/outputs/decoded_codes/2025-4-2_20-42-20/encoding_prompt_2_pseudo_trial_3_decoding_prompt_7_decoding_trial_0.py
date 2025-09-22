# Step 1: Input
# Accept two strings from the user
stringOne = input()  # First string
stringTwo = input()  # Second string

# Step 2: Process the Strings
# Create lists excluding spaces
filteredStringOne = [char for char in stringOne if char != ' ']
filteredStringTwo = [char for char in stringTwo if char != ' ']

# Step 3: Count Character Frequencies
# Initialize frequency difference list
frequencyDifference = []

# Iterate over the ASCII values from 'A' to 'z'
for char in range(ord('A'), ord('z') + 1):
    # Count occurrences in both filtered strings
    countInOne = filteredStringOne.count(chr(char))
    countInTwo = filteredStringTwo.count(chr(char))
    
    # Calculate the difference and append to frequencyDifference
    frequencyDifference.append(countInOne - countInTwo)

# Step 4: Check Frequency Conditions
# Create a list for negative counts
negativeCounts = [count for count in frequencyDifference if count < 0]

# Step 5: Output
if not negativeCounts:
    print("YES")  # No negative counts, so output YES
else:
    print("NO")   # There are negative counts, so output NO
