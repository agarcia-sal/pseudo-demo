# Start the process

# Get Input
desired_sum = abs(int(input()))  # Get user input, convert to absolute integer

# Initialize a Counter
counter = 0  # Set counter i to 0

# Loop Indefinitely
while True:
    # Calculate the sum of the first 'counter' integers
    sum_of_first_counter = (counter * (counter + 1)) // 2  # Use integer division for the sum

    # Determine the difference between the calculated sum and the desired sum
    difference = sum_of_first_counter - desired_sum

    # Check Conditions
    if sum_of_first_counter == desired_sum:
        print(counter)  # Print the value of counter, which is the answer
        break  # Exit the loop
    
    if sum_of_first_counter > desired_sum:
        if difference % 2 == 0:  # Check if the difference is even
            print(counter)  # Print counter as a potential answer
            break  # Exit the loop

    # Increment the Counter
    counter += 1  # Increase the value of counter by 1, moving to the next integer

# End the process
