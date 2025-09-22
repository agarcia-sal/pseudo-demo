# Initialize the target number and index
targetNumber = abs(int(input()))  # Read the input and get its absolute value
index = 0  # Initialize the index for summation

# Start an infinite loop to find the desired index
while True:
    # Calculate the sum of integers from 0 to index
    sumToIndex = (index * (index + 1)) // 2  # Use integer division for precision

    # Calculate the difference between sum and target
    difference = sumToIndex - targetNumber

    # Check for an exact match
    if sumToIndex == targetNumber:
        print(index)  # Print the current index if it matches the target
        break  # Exit the loop

    # Check if the sum exceeds the target
    if sumToIndex > targetNumber:
        # Check if the difference is even
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Print the index if the conditions are met
            break  # Exit the loop

    # Increment index to check the next number
    index += 1
