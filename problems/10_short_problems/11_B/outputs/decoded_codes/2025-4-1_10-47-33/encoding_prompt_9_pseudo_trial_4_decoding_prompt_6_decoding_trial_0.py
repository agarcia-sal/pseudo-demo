# Step 1: Receive input from the user and store its absolute value in target_value
target_value = abs(int(input()))

# Step 2: Initialize a counter to 0
counter = 0

# Step 3: Begin an infinite loop to find the solution
while True:
    # Step 4: Calculate the sum of the first 'counter' integers
    current_sum = counter * (counter + 1) // 2  # Using integer division

    # Step 5: Calculate the difference between current_sum and target_value
    difference = current_sum - target_value

    # Step 6: Check if current_sum equals target_value
    if current_sum == target_value:
        print(counter)  # Output the result and end the loop
        break

    # Step 7: Check if current_sum is greater than target_value
    if current_sum > target_value:
        # Check if the difference is even
        if difference % 2 == 0:
            print(counter)  # Output the result and end the loop
            break

    # Step 8: Increment the counter by 1
    counter += 1
