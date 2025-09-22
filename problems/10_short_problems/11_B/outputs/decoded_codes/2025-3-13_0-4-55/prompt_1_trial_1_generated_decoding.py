# 1. Initialize Variables
n = abs(int(input()))
i = 0  # Initialize the current integer candidate

# 2. Loop Indefinitely
while True:
    # a. Calculate Sum
    s = (i * (i + 1)) / 2  # Compute the sum of the first i integers
    
    # b. Determine Difference
    m = s - n  # Calculate the difference between sum and n
    
    # c. Check for Conditions
    if s == n:
        print(i)  # Print the current integer and exit
        break  # Exit the loop
        
    if s > n:
        if m % 2 == 0:  # Check if the difference is even
            print(i)  # Print the current integer and exit
            break  # Exit the loop
            
    # d. Increment Counter
    i += 1  # Increase i to check the next integer
