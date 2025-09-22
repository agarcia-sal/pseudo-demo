# Begin execution

# Step 1: Get the absolute value of an integer from user input
targetSum = abs(int(input()))

# Step 2: Initialize a counter variable
index = 0

# Step 3: Start an infinite loop
while True:
    # Step 3a: Calculate the sum of the first `index` integers
    sumOfIndices = (index * (index + 1)) / 2
    
    # Step 3b: Calculate the difference
    difference = sumOfIndices - targetSum
    
    # Step 3c: If sumOfIndices is equal to targetSum
    if sumOfIndices == targetSum:
        print(index)  # Print the value of index
        break  # Exit the loop

    # Step 3d: Else if sumOfIndices is greater than targetSum
    elif sumOfIndices > targetSum:
        # Check if difference is even
        if difference % 2 == 0:
            print(index)  # Print the value of index
            break  # Exit the loop
    
    # Step 3e: Increment index by 1
    index += 1

# End execution
