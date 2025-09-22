# Step 1: Input
# Read an integer value from the user
user_input = int(input())
# Step 2: Calculate the absolute value of the input
targetNumber = abs(user_input)

# Step 2: Initialize the counter variable
index = 0

# Step 3: Loop to calculate currentSum and check conditions
while True:
    # Calculate the sum of the first 'index' natural numbers
    currentSum = index * (index + 1) // 2  # Using integer division for exact result
    # Calculate the difference
    difference = currentSum - targetNumber
    
    # Step 3.3: Check Conditions
    if currentSum == targetNumber:
        # If currentSum matches targetNumber, print the index and exit
        print(index)
        break
    elif currentSum > targetNumber:
        # If currentSum is greater than targetNumber, check if the difference is even
        if difference % 2 == 0:
            # If difference is even, print the index and exit
            print(index)
            break
    
    # Increment the value of index by 1 for the next iteration
    index += 1
