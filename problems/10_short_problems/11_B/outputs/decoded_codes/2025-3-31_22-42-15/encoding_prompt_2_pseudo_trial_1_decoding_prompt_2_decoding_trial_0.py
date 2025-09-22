# Step 1: Get a number from the user and convert it to an integer
targetNumber = abs(int(input()))  # get absolute value

# Step 2: Initialize a counter variable
index = 0

# Step 3: Enter an infinite loop
while True:
    # Calculate the sum of the first `index` natural numbers
    sumOfFirstIndex = (index * (index + 1)) // 2  # use integer division

    # Calculate the difference from the target number
    difference = sumOfFirstIndex - targetNumber

    # Step 4: Check if the current sum equals the target number
    if sumOfFirstIndex == targetNumber:
        print(index)  # Print the index
        break  # Exit the loop

    # Step 5: Check if the current sum exceeds the target number
    if sumOfFirstIndex > targetNumber:
        # Check if the difference is even
        if difference % 2 == 0:  # check if the difference is even
            print(index)  # Print the index
            break  # Exit the loop

    # Step 6: Increment the counter variable
    index += 1

# Step 7: End of the program
