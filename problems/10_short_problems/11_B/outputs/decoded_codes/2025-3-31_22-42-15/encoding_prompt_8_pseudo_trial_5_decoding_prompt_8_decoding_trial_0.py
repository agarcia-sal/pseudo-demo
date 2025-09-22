# Start the process

# Get Input
desired_sum = abs(int(input()))

# Initialize a Counter
i = 0

# Loop Indefinitely
while True:
    # Calculate the sum of the first 'i' integers
    sum_of_first_i = (i * (i + 1)) // 2
    
    # Determine the difference
    difference = sum_of_first_i - desired_sum
    
    # Check Conditions
    if sum_of_first_i == desired_sum:
        print(i)
        break
    
    if sum_of_first_i > desired_sum:
        if difference % 2 == 0:
            print(i)
            break
    
    # Increment the Counter
    i += 1

# End the process
