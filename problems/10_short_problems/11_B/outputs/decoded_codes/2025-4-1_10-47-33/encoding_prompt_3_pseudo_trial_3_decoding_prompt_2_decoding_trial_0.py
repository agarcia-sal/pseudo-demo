# Step 1: Get the absolute value of input and convert it to an integer
target_value = abs(int(input()))

# Step 2: Initialize counter variable
index = 0

# Step 3: Start an infinite loop to find the value
while True:
    
    # Calculate the sum of first 'index' natural numbers
    sum_value = (index * (index + 1)) // 2  # Using integer division
    
    # Calculate the difference between the sum and the target_value
    difference = sum_value - target_value
    
    # Step 4: Check if the sum matches the target_value
    if sum_value == target_value:
        print(index)  # Output the current index and exit the loop
        break
    
    # Step 5: Check if the sum exceeds the target_value
    elif sum_value > target_value:
        
        # Step 6: Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the current index and exit the loop
            break
    
    # Increment the index for the next iteration
    index += 1
