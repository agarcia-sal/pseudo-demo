# START

# Read an integer input from the user, ensuring it is non-negative
number = abs(int(input()))

# Initialize a counter variable
counter = 0

# Infinite loop to calculate and check certain conditions
while True:
    # Calculate the sum of the first 'counter' natural numbers
    sum = (counter * (counter + 1)) // 2
    
    # Determine the difference between the calculated sum and the input number
    difference = sum - number

    # Check if the calculated sum equals the input number
    if sum == number:
        # Print the current counter value as the result
        print(counter)
        break  # Exit the loop
    
    # Check if the calculated sum exceeds the input number
    elif sum > number:
        # Check if the difference is an even number
        if difference % 2 == 0:
            # Print the current counter value as the result
            print(counter)
            break  # Exit the loop

    # Increment the counter for the next iteration
    counter += 1

# END
