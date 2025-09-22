# Step 1: Start

# Step 2: Get User Input
# Convert the user-provided input to an integer
desiredNumber = abs(int(input()))

# Step 3: Initialize Variables
index = 0

# Step 4: Begin Loop (indefinitely)
while True:
    # Calculate the sum of all integers from 1 to index
    currentSum = (index * (index + 1)) / 2
    
    # Calculate the difference between currentSum and desiredNumber
    difference = currentSum - desiredNumber
    
    # Check Conditions
    if currentSum == desiredNumber:
        # Print the value of index
        print(index)
        break  # Exit the loop
    elif currentSum > desiredNumber:
        # If difference is even
        if difference % 2 == 0:
            # Print the value of index
            print(index)
            break  # Exit the loop

    # Increment the index by 1
    index += 1

# Step 5: End Loop

# Step 6: End Program
