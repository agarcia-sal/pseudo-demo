# Start the Program

# Step 2: Receive Input
# Prompt the user to enter the first set of three numbers
firstSet = input()
# Prompt the user to enter the second set of three numbers
secondSet = input()

# Step 3: Split Input into Individual Numbers
# Split the input strings into lists of strings
firstList = firstSet.split()
secondList = secondSet.split()

# Step 4: Initialize a Counter for Differences
# Initialize difference count
differenceCount = 0

# Step 5: Compare Each Number in the Sets
# Loop through each index from 0 to 2
for index in range(3):
    # Convert numbers to integers
    firstNumber = int(firstList[index])
    secondNumber = int(secondList[index])
    
    # Check if the numbers are different
    if firstNumber != secondNumber:
        # Increment the difference count
        differenceCount += 1

# Step 6: Determine the Result
# If the number of differences is less than 3
if differenceCount < 3:
    print("YES")  # Output YES if fewer than 3 differences
else:
    print("NO")   # Otherwise, output NO

# End the Program
