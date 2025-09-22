# Start of the program

# Read input value and convert it to a positive integer
target_number = abs(int(input()))

# Initialize a counter to track the current step
step_counter = 0

# Start an infinite loop to find the solution
while True:
    # Calculate the sum of the first 'step_counter' natural numbers
    current_sum = (step_counter * (step_counter + 1)) // 2

    # Calculate the difference between current_sum and target_number
    difference = current_sum - target_number

    # Check if the current_sum is equal to the target_number
    if current_sum == target_number:
        print(step_counter)  # Output the step_counter
        break  # Exit the loop

    # Check if current_sum is greater than target_number
    elif current_sum > target_number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(step_counter)  # Output the step_counter
            break  # Exit the loop

    # Increment the step_counter for the next iteration
    step_counter += 1

# End of the program
