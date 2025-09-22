def find_integer(n):
    # Convert input to an absolute integer
    n = abs(int(input()))  # Ensure n is an absolute value, based on user input
    
    # Initialize a counter
    i = 0
    
    # Start an infinite loop
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Sum using the formula for the triangular number
        
        # Determine the difference between the sum and n
        m = s - n
        
        # Check if the sum equals n
        if s == n:
            print(i)  # Print the current value of i and exit the loop
            break
        
        # Check if the sum is greater than n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)  # Print the current value of i and exit the loop
                break
        
        # Increment the counter for the next iteration
        i += 1  # Increment i by 1 for the next iteration

# Example usage: 
# Uncomment the following line to test the function
# find_integer()
