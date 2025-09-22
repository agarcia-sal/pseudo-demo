# Start the process

# Get Input
desired_sum = abs(int(input()))

# Initialize a Counter
i = 0

# Loop Indefinitely
while True:
    # Calculate the sum of the first i integers
    sum_of_first_i = (i * (i + 1)) / 2
    
    # Determine the difference between the calculated sum and the desired sum
    difference = sum_of_first_i - desired_sum

    # Check Conditions
    if sum_of_first_i == desired_sum:
        print(i)  # Print the value of 'i'
        break  # Exit the loop

    if sum_of_first_i > desired_sum:
        if difference % 2 == 0:  # Check if the difference is even
            print(i)  # Print the value of 'i'
            break  # Exit the loop
    
    # Increment the Counter
    i += 1

# End the process
