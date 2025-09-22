def findMinimumInteger():
    # Read an integer input and ensure it is non-negative
    n = abs(int(input()))

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

# Example test cases (uncomment to test)
# Find minimum integer for 0
# findMinimumInteger() # Output: 0
# Find minimum integer for 3
# findMinimumInteger() # Output: 2
