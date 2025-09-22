# Start the program
# Get the absolute value of user input as an integer, assign it to `n`
n = abs(int(input()))

# Initialize `i` to 0
i = 0

# Enter an infinite loop
while True:
    # Calculate the sum `s` of the first `i` natural numbers
    s = i * (i + 1) // 2  # Using integer division to ensure `s` is an integer
    
    # Calculate the difference `m` between `s` and `n`
    m = s - n
    
    # Check if `s` is equal to `n`
    if s == n:
        print(i)
        break  # Exit the loop if equal
    
    # Check if `s` is greater than `n`
    if s > n:
        # Check if `m` is even
        if m % 2 == 0:
            print(i)
            break  # Exit the loop if `m` is even
    
    # Increment `i` by 1
    i += 1
