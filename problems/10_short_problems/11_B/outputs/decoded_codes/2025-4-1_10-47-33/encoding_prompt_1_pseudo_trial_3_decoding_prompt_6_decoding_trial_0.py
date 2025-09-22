# Step 1: Import the math library for absolute value function
# (Not strictly necessary since we can use built-in abs in Python)
import math

# Step 2: Read input and initialize variables
n = abs(int(input()))  # Initialize n to the absolute value of the input integer
i = 0  # Initialize i to 0, to be used for calculating sum of natural numbers

# Step 3: Start an infinite loop to calculate sequence
while True:
    # Calculate the sum of the first i natural numbers
    s = i * (i + 1) // 2  # Use integer division for the sum
    m = s - n  # Calculate m as the difference between s and n

    # Check if the sum s equals n
    if s == n:
        print(i)  # Print the value of i and exit the loop
        break  # Exit loop

    # Check if the sum s is greater than n
    if s > n:
        # Check if m is even
        if m % 2 == 0:
            print(i)  # Print the value of i and exit the loop
            break  # Exit loop

    # Increment the value of i for the next iteration
    i += 1
