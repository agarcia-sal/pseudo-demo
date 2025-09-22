def find_integer():
    # Get the absolute value of the input
    n = abs(int(input()))
    
    # Initialize a counter
    i = 0
    
    # Start an infinite loop
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2
        
        # Determine the difference between the sum and n
        m = s - n
        
        # Check if the sum equals n
        if s == n:
            print(i)
            break
        
        # Check if the sum is greater than n
        elif s > n:
            # Check if the difference is even
            if m % 2 == 0:
                print(i)
                break
            
        # Increment the counter for the next iteration
        i += 1

# Testing
# Example test cases are mentioned below:
# Input: 0 should output 0
# Input: 5 should output 5
# Input: 10 should output 4
# The function can be tested by directly feeding inputs while calling.
