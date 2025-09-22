def find_integer():
    # Take an absolute integer input
    n = abs(int(input()))
    
    # Initialize iteration variable
    i = 0 
    
    # Start an indefinite loop
    while True:
        # Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2
        
        # Calculate the difference between s and n
        m = s - n
        
        # Check if the calculated sum s is equal to n
        if s == n:
            print(i)   # Print the integer i
            break  # Exit the loop
        
        # Check if the calculated sum s is greater than n
        elif s > n:
            # Check if the difference m is even
            if m % 2 == 0:
                print(i)   # Print the integer i
                break  # Exit the loop
        
        # Increment i for the next iteration
        i += 1 

# Test cases can be added here in comments
# find_integer()  # Example input: 5
# find_integer()  # Example input: 10
# find_integer()  # Example input: -3
