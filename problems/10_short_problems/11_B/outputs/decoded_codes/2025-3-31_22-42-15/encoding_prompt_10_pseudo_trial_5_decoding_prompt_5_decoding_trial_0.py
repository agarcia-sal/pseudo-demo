# Function to find the smallest integer i such that the sum of the first i natural numbers
# is equal to a given positive integer n or can be made equal by adjusting with an even difference.
def find_smallest_integer():
    # Step 1: Initialize variables
    n = 0  # The input positive integer
    i = 0  # Iterator for natural numbers
    
    # Step 2: Get user input
    n = abs(int(input()))  # Read and convert input to a positive integer
    
    # Step 3: Infinite loop to find the solution
    while True:
        # Step 4: Calculate the sum of the first i natural numbers
        s = (i * (i + 1)) // 2  # Sum of first i integers
        
        # Step 5: Calculate m as the difference between s and n
        m = s - n
        
        # Step 6: Check if the sum is equal to the input n
        if s == n:
            print(i)  # Output the result
            break  # Exit the loop

        # Step 7: Check if the sum exceeds the input n
        elif s > n:
            # Step 8: Check if the difference m is even
            if m % 2 == 0:
                print(i)  # Output the result
                break  # Exit the loop
        
        # Step 9: Increment i for the next iteration
        i += 1

# Sample usage (uncomment to run):
# find_smallest_integer()

# Consider edge cases like n = 0 or n = 1:
# find_smallest_integer()  # Test with various inputs for additional validation
