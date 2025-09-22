# BEGIN

# Step 1: Get the absolute value of input and convert it to an integer
targetValue = abs(int(input()))

# Step 2: Initialize counter variable
index = 0

# Step 3: Start an infinite loop to find the value
while True:
    
    # Calculate the sum of first 'index' natural numbers
    sum = (index * (index + 1)) // 2  # Integer division

    # Calculate the difference between the sum and the targetValue
    difference = sum - targetValue

    # Step 4: Check if the sum matches the targetValue
    if sum == targetValue:
        print(index)  # Output the current index and exit the loop
        break

    # Step 5: Check if the sum exceeds the targetValue
    elif sum > targetValue:
        
        # Step 6: Check if the difference is even
        if difference % 2 == 0:  # Even check
            print(index)  # Output the current index and exit the loop
            break

    # Increment the index for the next iteration
    index += 1

# END
