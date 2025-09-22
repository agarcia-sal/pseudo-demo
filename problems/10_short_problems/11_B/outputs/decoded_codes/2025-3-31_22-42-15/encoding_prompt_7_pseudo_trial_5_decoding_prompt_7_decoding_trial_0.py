def find_integer():
    # Read input and convert it to an absolute integer
    n = abs(int(input()))
    
    # Initialize a counter for natural numbers
    i = 0

    # Start an infinite loop to find the result
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Using integer division
        
        # Calculate the difference between the sum and n
        m = s - n
        
        # Check if the calculated sum equals the input number
        if s == n:
            # Print the current value of i if the sum matches
            print(i)
            break
        
        # Check if the sum is greater than n
        elif s > n:
            # If the difference is even
            if m % 2 == 0:
                # Print the current value of i when condition is met
                print(i)
                break
        
        # Increment the counter for the next iteration
        i += 1

# Uncomment the next line to test the function directly
# find_integer()
