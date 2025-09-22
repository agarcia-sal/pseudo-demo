# Start of the program

# Step 2: Read an integer value from the user and store its absolute value as target_sum
target_sum = abs(int(input()))

# Step 3: Initialize a counter index to 0
index = 0

# Step 4: Begin an infinite loop
while True:
    # Step 4.1: Calculate the sum of the first index natural numbers
    current_sum = index * (index + 1) // 2  # Using integer division

    # Step 4.2: Calculate the difference between current_sum and target_sum
    difference = current_sum - target_sum
    
    # Step 4.3: Check for exact match
    if current_sum == target_sum:
        # Output the value of index
        print(index)
        break  # Terminate loop
    
    # Step 4.4: Check for overshoot
    if current_sum > target_sum:
        # Check if the difference is even
        if difference % 2 == 0:
            # Output the value of index
            print(index)
            break  # Terminate loop
    
    # Step 4.5: Increment index by 1
    index += 1

# End of the program
