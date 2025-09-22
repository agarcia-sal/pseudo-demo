# Start the process

# Get Input: Prompt the user for a number and convert it to an absolute integer
desired_sum = abs(int(input()))

# Initialize a Counter: Set 'i' to 0
i = 0

# Loop Indefinitely: Repeat until a condition is met
while True:
    # Calculate the sum_of_first_i using the formula
    sum_of_first_i = (i * (i + 1)) // 2
    
    # Determine the difference between the calculated sum and the desired sum
    difference = sum_of_first_i - desired_sum
    
    # Check Conditions
    if sum_of_first_i == desired_sum:
        # If the sum equals the desired sum, print 'i' and exit
        print(i)
        break
    
    if sum_of_first_i > desired_sum:
        # If the sum is greater than the desired sum
        if difference % 2 == 0:
            # If the difference is even, print 'i' and exit
            print(i)
            break
    
    # Increment the Counter: Increase 'i' by 1
    i += 1

# End the process
