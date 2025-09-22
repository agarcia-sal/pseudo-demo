# Step 1: Get a number from the user and convert it to an integer
targetNumber = abs(int(input()))

# Step 2: Initialize a counter variable `index` to 0
index = 0

# Step 3: Enter an infinite loop
while True:
    # Calculate the sum of the first `index` natural numbers
    sumOfFirstIndex = (index * (index + 1)) // 2
    
    # Calculate the difference
    difference = sumOfFirstIndex - targetNumber
    
    # Step 4: Check if the current sum equals the target number
    if sumOfFirstIndex == targetNumber:
        print(index)
        break  # Exit the loop

    # Step 5: Check if the current sum exceeds the target number
    if sumOfFirstIndex > targetNumber:
        # Check if `difference` is an even number
        if difference % 2 == 0:
            print(index)
            break  # Exit the loop
            
    # Step 6: Increment the counter variable `index` by 1
    index += 1

# Step 7: End - The loop will end with a break statement
