# Step 1: Start the Program

# Step 2: Receive Input
firstSet = input()  # User inputs the first set of numbers
secondSet = input()  # User inputs the second set of numbers

# Step 3: Split Input into Individual Numbers
firstList = firstSet.split()  # Split the first set into a list
secondList = secondSet.split()  # Split the second set into a list

# Step 4: Initialize a Counter for Differences
differenceCount = 0  # Initialize the counter for differences

# Step 5: Compare Each Number in the Sets
for index in range(3):  # Loop through indices 0 to 2
    firstNumber = int(firstList[index])  # Convert to integer
    secondNumber = int(secondList[index])  # Convert to integer
    if firstNumber != secondNumber:  # Check for difference
        differenceCount += 1  # Increment the counter if different

# Step 6: Determine the Result
if differenceCount < 3:
    print("YES")  # Print "YES" if differences are fewer than 3
else:
    print("NO")  # Print "NO" if differences are 3 or more

# Step 7: End the Program
