def find_integer(n):
    # Convert input to an absolute integer
    n = abs(int(input()))
    
    # Initialize a counter
    i = 0

    # Start an infinite loop
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Using // for integer division
        
        # Determine the difference between the sum and n
        m = s - n
        
        # Check if the sum equals n
        if s == n:
            # Print the current value of i and exit the loop
            print(i)
            break
        
        # Check if the sum is greater than n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                # Print the current value of i and exit the loop
                print(i)
                break
            
        # Increment the counter for the next iteration
        i += 1
