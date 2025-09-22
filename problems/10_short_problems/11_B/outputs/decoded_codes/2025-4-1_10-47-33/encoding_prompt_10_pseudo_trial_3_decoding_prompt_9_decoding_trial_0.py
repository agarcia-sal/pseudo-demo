# Assume 'n' is a non-negative integer input by the user.
n = abs(int(input()))  # Read and convert the input to an absolute non-negative integer
i = 0  # Initialize the counter

# Begin an infinite loop
while True:
    # Calculate the sum of the first 'i' integers using the formula
    s = (i * (i + 1)) // 2  # Use integer division for accuracy

    # Calculate the difference between 's' and 'n'
    m = s - n
    
    # Check if the sum 's' is equal to 'n'
    if s == n:
        print(i)  # Output the value of 'i'
        break  # Exit the loop

    # Check if the sum 's' is greater than 'n'
    elif s > n:
        # Check if the difference 'm' is even
        if m % 2 == 0:
            print(i)  # Output the value of 'i'
            break  # Exit the loop

    # Increment 'i' for the next iteration
    i += 1
