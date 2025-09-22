# Start of the program
# Step 2: Get input from the user for the target sum and store its absolute value
targetSum = abs(int(input()))

# Step 3: Initialize index to 0
index = 0

# Step 4: Repeat indefinitely
while True:
    # Step 4a: Calculate the sum of the first 'index' natural numbers
    currentSum = (index * (index + 1)) // 2

    # Step 4b: Calculate the difference between currentSum and targetSum
    difference = currentSum - targetSum

    # Step 4c: Check if currentSum equals targetSum
    if currentSum == targetSum:
        print(index)  # Print the current value of index
        break  # Exit the loop

    # Step 4d: Check if currentSum is greater than targetSum
    if currentSum > targetSum:
        # Step 4d: Check if the difference is an even number
        if difference % 2 == 0:
            print(index)  # Print the current value of index
            break  # Exit the loop

    # Step 4e: Increment index
    index += 1

# End of the program
