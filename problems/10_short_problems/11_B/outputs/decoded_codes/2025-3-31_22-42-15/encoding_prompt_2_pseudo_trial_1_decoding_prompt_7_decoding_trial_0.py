# Step 1: Get user input and initialize target variable
targetNumber = abs(int(input()))  # Getting the absolute value of the input number

# Step 2: Initialize index variable
index = 0  # This will keep track of the current index in the natural numbers

# Step 3: Enter an infinite loop
while True:
    # Step 4: Calculate the sum of the first 'index' natural numbers
    sumOfFirstIndex = (index * (index + 1)) // 2  # Using integer division for the sum

    # Step 5: Calculate the difference from the target number
    difference = sumOfFirstIndex - targetNumber

    # Step 6: Check if the current sum equals the target number
    if sumOfFirstIndex == targetNumber:
        print(index)  # Print index if sum matches target
        break  # Exit the loop

    # Step 7: Check if the current sum exceeds the target number
    if sumOfFirstIndex > targetNumber:
        # Step 8: If difference is even, print the value of index
        if difference % 2 == 0:
            print(index)  # Print index if difference is even
            break  # Exit the loop

    # Step 9: Increment the index for the next iteration
    index += 1  # Move to the next natural number
