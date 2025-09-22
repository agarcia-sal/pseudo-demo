# Start the process

# Get Input
desired_sum = abs(int(input()))

# Initialize a Counter
i = 0

# Loop Indefinitely
while True:
    # Calculate the sum_of_first_i as the sum of all integers from 1 to 'i'
    sum_of_first_i = (i * (i + 1)) // 2  # Using integer division for clarity

    # Determine the difference between the calculated sum and the desired sum
    difference = sum_of_first_i - desired_sum

    # Check Conditions
    if sum_of_first_i == desired_sum:
        print(i)  # This is the answer, sum matches desired_sum
        break
    
    if sum_of_first_i > desired_sum:
        if difference % 2 == 0:  # Check if the difference is even
            print(i)  # This is also a potential answer
            break

    # Increment the Counter
    i += 1

# End the process
