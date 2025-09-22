# Step 1: Receive Input
target_value = abs(int(input()))  # Convert input to absolute integer

# Step 2: Initialize Variables
index = 0  # This serves as a counter

# Step 3: Infinite Loop
while True:  # We will loop indefinitely until we find the solution
    # Calculate Sum
    current_sum = (index * (index + 1)) // 2  # Sum of integers from 0 to index

    # Calculate Difference
    diff = current_sum - target_value  # Difference between current sum and target value
    
    # Check for Equality
    if current_sum == target_value:
        print(index)  # Output the value of index
        break  # Exit the loop if we find an exact match

    # Check for Greater Sum
    if current_sum > target_value:
        if diff % 2 == 0:  # Check if the difference is even
            print(index)  # Output the value of index
            break  # Exit the loop if the difference from targetValue is even

    # Increment Index
    index += 1  # Move to the next integer
