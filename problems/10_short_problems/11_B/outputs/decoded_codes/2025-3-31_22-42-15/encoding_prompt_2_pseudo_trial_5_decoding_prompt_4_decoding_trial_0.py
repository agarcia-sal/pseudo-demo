# Step 1: Read an integer from the user and store its absolute value
targetSum = abs(int(input()))

# Step 2: Initialize a counter variable
currentIndex = 0

# Step 3: Start an infinite loop to find the suitable index
while True:
    # Step 4: Calculate the sum of the first currentIndex integers
    sumOfSeries = (currentIndex * (currentIndex + 1)) // 2
    
    # Step 5: Calculate the difference between sumOfSeries and targetSum
    difference = sumOfSeries - targetSum
    
    # Step 6: Check the conditions
    if sumOfSeries == targetSum:
        print(currentIndex)
        break  # Condition met, exit the loop
    
    if sumOfSeries > targetSum:
        if difference % 2 == 0:
            print(currentIndex)
            break  # Condition met, exit the loop
    
    # Step 7: Increment the counter
    currentIndex += 1
