# Start the program

# Get the absolute value of user input as an integer and assign it to `n`
n = abs(int(input()))

# Initialize `i` to 0
i = 0

# Enter an infinite loop
while True:
    # Calculate the sum `s` of the first `i` natural numbers
    s = i * (i + 1) // 2  # Using integer division for correct sum calculation

    # Calculate the difference `m` between `s` and `n`
    m = s - n  # This represents how far `s` is from `n`
    
    # Check if `s` is equal to `n`
    if s == n:
        print(i)  # Print the value of `i` and exit the loop
        break
    
    # Check if `s` is greater than `n`
    if s > n:
        # If this condition holds true, then check if `m` is even
        if m % 2 == 0:  # Check if `m` is even
            print(i)  # Print the value of `i` and exit the loop
            break
    
    # Increment `i` by 1
    i += 1

# End of program
