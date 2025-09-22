# Start the program
n = abs(int(input()))  # Get the absolute value of user input as an integer, assign it to `n`
i = 0  # Initialize `i` to 0

while True:  # Enter an infinite loop
    s = i * (i + 1) // 2  # Calculate the sum `s` of the first `i` natural numbers
    m = s - n  # Calculate the difference `m` between `s` and `n`
    
    if s == n:  # Check if `s` is equal to `n`
        print(i)  # Print the value of `i` and exit the loop
        break  # Exit the loop
    
    if s > n:  # Check if `s` is greater than `n`
        if m % 2 == 0:  # Check if `m` is even
            print(i)  # Print the value of `i` and exit the loop
            break  # Exit the loop
    
    i += 1  # Increment `i` by 1
# End of program
