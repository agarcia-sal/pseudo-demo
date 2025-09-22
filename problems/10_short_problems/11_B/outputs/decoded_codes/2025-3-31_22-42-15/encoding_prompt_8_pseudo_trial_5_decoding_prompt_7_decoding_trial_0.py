# Start the process

# Get Input
desired_sum = abs(int(input()))  # Prompt the user for a number and store it as an absolute integer

# Initialize a Counter
i = 0  # This counter will track the number of terms

# Loop Indefinitely
while True:
    # Calculate the sum of the first 'i' natural numbers using the formula
    sum_of_first_i = (i * (i + 1)) // 2  # Integer division to get the sum

    # Determine the difference between the calculated sum and the desired sum
    difference = sum_of_first_i - desired_sum

    # Check Conditions
    if sum_of_first_i == desired_sum:
        print(i)  # Print the value of 'i' if sums are equal
        break  # Exit the loop

    if sum_of_first_i > desired_sum:
        if difference % 2 == 0:  # Check if the difference is even
            print(i)  # Print the value of 'i' if the even difference condition is satisfied
            break  # Exit the loop

    # Increment the Counter
    i += 1  # Move to the next integer

# End the process
