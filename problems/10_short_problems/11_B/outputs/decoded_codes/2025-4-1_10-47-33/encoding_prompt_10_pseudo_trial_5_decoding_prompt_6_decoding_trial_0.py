# Import the required functions from the math library
from math import fabs

# Read an integer input and store the absolute value
n = fabs(int(input()))

# Initialize the variable i to 0
i = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first i integers
    s = (i * (i + 1)) / 2
    
    # Calculate the difference between the sum and n
    m = s - n
    
    # Check if the sum equals n
    if s == n:
        print(i)  # Output the value of i
        break  # Exit the loop
        
    # Check if the sum exceeds n
    elif s > n:
        # Check if the difference is even
        if m % 2 == 0:
            print(i)  # Output the value of i
            break  # Exit the loop
            
    # Increment i by 1
    i += 1
