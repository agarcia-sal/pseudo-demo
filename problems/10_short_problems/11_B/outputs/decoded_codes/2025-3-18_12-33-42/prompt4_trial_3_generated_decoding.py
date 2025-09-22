def find_integer():
    # Get user input and calculate its absolute value
    n = abs(int(input()))
    i = 0
    
    # Infinite loop to find the required integer
    while True:
        # Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2  # Using integer division for clarity
        m = s - n
        
        # Check if we have found the exact match
        if s == n:
            print(i)  # Output the resulting integer
            break
        
        # Check if the sum exceeds the input value
        if s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Output the resulting integer
                break
                
        # Increment i for the next iteration
        i += 1

# Testing the function with various cases
# Uncomment the following line to execute
# find_integer()
