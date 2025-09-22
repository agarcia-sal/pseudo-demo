# Read a number from user input and take its absolute value
number_to_check = abs(int(input()))

# Initialize a counter variable
counter = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first 'counter' numbers
    sum_of_numbers = (counter * (counter + 1)) / 2
    
    # Calculate the difference between sum and the number to check
    difference = sum_of_numbers - number_to_check

    # Check if the current sum equals the number to check
    if sum_of_numbers == number_to_check:
        print(counter)  # Output the current counter value
        break  # Exit the loop

    # Check if the current sum exceeds the number to check
    elif sum_of_numbers > number_to_check:
        # Check if the difference is even
        if difference % 2 == 0:
            print(counter)  # Output the current counter value
            break  # Exit the loop

    # Increment the counter for the next iteration
    counter += 1
