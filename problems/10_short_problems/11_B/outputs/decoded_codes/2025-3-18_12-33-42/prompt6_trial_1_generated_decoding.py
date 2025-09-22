# Step 1: Start the program

# Step 2: Read an integer input and calculate its absolute value
number_input = int(input())  # Read an integer from user input
target_value = abs(number_input)  # Calculate the absolute value

# Step 3: Initialize a counter to 0
counter = 0

# Step 4: Begin an infinite loop
while True:
    # Step 5: Calculate the current sum of the first 'counter' integers
    current_sum = (counter * (counter + 1)) // 2  # Sum calculation using the formula

    # Step 6: Compute the difference
    difference = current_sum - target_value

    # Step 7: Check conditions
    if current_sum == target_value:
        print(counter)  # Print the value of counter if sum equals target
        break  # Exit the loop

    elif current_sum > target_value:
        if difference % 2 == 0:  # Check if the difference is even
            print(counter)  # Print the value of counter
            break  # Exit the loop

    # Step 8: Increment the counter for the next iteration
    counter += 1

# Step 9: End the program (implicitly done when leaving the loop)
