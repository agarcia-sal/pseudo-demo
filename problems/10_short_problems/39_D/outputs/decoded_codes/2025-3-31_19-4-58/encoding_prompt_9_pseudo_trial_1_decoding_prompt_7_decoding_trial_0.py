# Start Program

# Step 2: Receive Input
# Read the first line of input and store it as the first set of values (firstSet)
firstSet = input()
# Read the second line of input and store it as the second set of values (secondSet)
secondSet = input()

# Step 3: Process Input
# Split firstSet into individual values
firstSet = firstSet.split()
# Split secondSet into individual values
secondSet = secondSet.split()

# Step 4: Initialize Difference Counter
# Set a variable called differenceCount to 0 to keep track of how many values differ between the two sets
differenceCount = 0

# Step 5: Compare Values
# For each index from 0 to 2 (inclusive)
for i in range(3):
    # Convert the value from firstSet at this index to a number (firstValue)
    firstValue = int(firstSet[i])
    # Convert the value from secondSet at this index to a number (secondValue)
    secondValue = int(secondSet[i])
    
    # If firstValue is not equal to secondValue
    if firstValue != secondValue:
        # Increment the differenceCount by 1
        differenceCount += 1

# Step 6: Determine Result
# If differenceCount is less than 3
if differenceCount < 3:
    # Output "YES" indicating the sets differ in fewer than three positions
    print("YES")
else:
    # Otherwise output "NO" indicating the sets differ in three or more positions
    print("NO")

# End Program


    1 2 3
    1 2 3
    

    YES
    

    1 2 3
    4 5 6
    

    NO
    

    7 8 9
    7 5 9
    

    YES
    