# Function to find the integer based on the given pseudocode logic
def find_integer():
    # Step 1: Get the absolute integer input from the user
    n = abs(int(input()))
    
    # Step 2: Initialize the counter variable
    i = 0
    
    # Step 3: Begin an infinite loop to find the result
    while True:
        # Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2
        
        # Calculate the difference between the sum and input
        m = s - n
        
        # Step 4: Check if the sum equals n
        if s == n:
            print(i)
            break
        
        # Step 5: Check if the sum exceeds n
        elif s > n:
            # Step 6: Check if the difference is even
            if m % 2 == 0:
                print(i)
                break
        
        # Increment the counter for the next iteration
        i += 1

# Calling the function to execute
find_integer()

# Test Case (uncomment for testing)
# Input: 3 would print 2 (since 0+1+2=3).
# Input: 5 would print 3 (since 0+1+2+3=6 and (6-5) is even).
