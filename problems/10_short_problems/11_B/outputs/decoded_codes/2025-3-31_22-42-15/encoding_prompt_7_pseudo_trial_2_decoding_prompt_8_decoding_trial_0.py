def findMinimumInteger():
    n = abs(int(input()))  # Get absolute value of integer input

    i = 0  # Initialize counter variable

    while True:  # Start an infinite loop
        s = (i * (i + 1)) // 2  # Calculate the sum of the first i integers
        m = s - n  # Calculate the difference between sum s and n
        
        if s == n:  # Check if sum s is equal to n
            print(i)  # Output the current value of i
            break  # Exit the loop
            
        elif s > n:  # Check if sum s exceeds n
            if m % 2 == 0:  # Check if the difference m is even
                print(i)  # Output the current value of i
                break  # Exit the loop
                
        i += 1  # Increment counter for the next iteration

# Example usage (uncomment the next line to run)
# findMinimumInteger()
