# Start of the program

# Read an integer input from the user and ensure it is non-negative
number = abs(int(input()))  # Getting input from user and taking the absolute value

# Initialize a counter variable
counter = 0

# Infinite loop to calculate and check certain conditions
while True:
    # Calculate the sum of the first 'counter' natural numbers
    sum_of_natural_numbers = (counter * (counter + 1)) // 2  # Integer division for sum

    # Determine the difference between the calculated sum and the input number
    difference = sum_of_natural_numbers - number

    # Check if the calculated sum equals the input number
    if sum_of_natural_numbers == number:
        # Print the current counter value as the result
        print(counter)
        break  # Exit the loop

    # Check if the calculated sum exceeds the input number
    elif sum_of_natural_numbers > number:
        # Check if the difference is an even number
        if difference % 2 == 0:  # Check if difference is even
            # Print the current counter value as the result
            print(counter)
            break  # Exit the loop

    # Increment the counter for the next iteration
    counter += 1  # Increment counter by 1

# End of the program
