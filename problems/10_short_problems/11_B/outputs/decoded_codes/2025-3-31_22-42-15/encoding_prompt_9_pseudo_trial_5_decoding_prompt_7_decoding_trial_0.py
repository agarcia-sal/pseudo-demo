# This program finds the smallest non-negative integer i such that the sum of the first i integers 
# is equal to or can be split evenly from the surplus when it exceeds a given non-negative integer n.
 
# Step 1: Receive Input
targetSum = int(input())  # Get a non-negative integer value from the user

# Step 2: Initialize Variables
currentIndex = 0  # Track the current integer being processed

# Step 3: Infinite Loop
while True:
    # Step 3.1: Calculate the Sum
    currentSum = (currentIndex * (currentIndex + 1)) // 2  # Calculate sum of first currentIndex integers
    
    # Step 3.2: Calculate the Difference
    surplus = currentSum - targetSum  # Calculate surplus
    
    # Step 3.3: Check for Exact Match
    if currentSum == targetSum:
        print(currentIndex)  # Print currentIndex as solution
        break  # Exit loop
    
    # Step 3.4: Check for Surplus Condition
    if surplus > 0:  # If currentSum exceeds targetSum
        if surplus % 2 == 0:  # Check if surplus can be evenly divided by 2
            print(currentIndex)  # Print currentIndex as solution
            break  # Exit loop
            
    # Step 3.5: Increment Index
    currentIndex += 1  # Move to the next integer
