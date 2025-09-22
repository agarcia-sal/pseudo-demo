# Start of the code

# Get the absolute value of the input and store it as a number
number = abs(int(input()))

# Initialize a counter variable
counter = 0

# Enter an infinite loop to repeatedly check conditions
while True:
    # Calculate the triangular number for the current counter value
    triangularNumber = (counter * (counter + 1)) // 2

    # Calculate the difference between the triangular number and the input number
    difference = triangularNumber - number

    # Check if the triangular number is equal to the input number
    if triangularNumber == number:
        # Print the current counter as the result
        print("The result is:", counter)
        # Exit the loop since the condition is satisfied
        break

    # Check if the triangular number is greater than the input number
    elif triangularNumber > number:
        # Check if the difference is an even number
        if difference % 2 == 0:
            # Print the current counter as the result since the condition is met
            print("The result is:", counter)
            # Exit the loop since the condition is satisfied
            break

    # Increment the counter for the next iteration
    counter += 1

# End of the code
