def findMinimumInteger(n):
    # Ensure n is a non-negative integer
    n = abs(int(input()))  # Read input and take its absolute value

    # Initialize counter variable
    i = 0

    # Start an infinite loop
    while True:
        # Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2
        
        # Calculate the difference between sum s and n
        m = s - n
        
        # Check if sum s is equal to n
        if s == n:
            print(i)  # Output the current value of i
            break  # Exit the loop
            
        # Check if sum s exceeds n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:
                print(i)  # Output the current value of i
                break  # Exit the loop
        
        # Increment counter for the next iteration
        i += 1

# Call the function to execute the code
findMinimumInteger(0)  # Initial call to function; the actual value of n will be read from input
