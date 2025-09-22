# Start of the program

# Read an integer input from the user, ensuring it is non-negative
number = abs(int(input()))  # Use abs to ensure the number is non-negative

# Initialize a counter variable
counter = 0

# Infinite loop to calculate and check certain conditions
while True:
    # Calculate the sum of the first 'counter' natural numbers
    sum_value = (counter * (counter + 1)) // 2  # Use integer division

    # Determine the difference between the calculated sum and the input number
    difference = sum_value - number

    # Check if the calculated sum equals the input number
    if sum_value == number:
        # Print the current counter value as the result
        print(counter)
        break  # Exit the loop
    
    # Check if the calculated sum exceeds the input number
    elif sum_value > number:
        # Check if the difference is an even number
        if difference % 2 == 0:  # Check if difference is even
            # Print the current counter value as the result
            print(counter)
            break  # Exit the loop

    # Increment the counter for the next iteration
    counter += 1

# End of the program
