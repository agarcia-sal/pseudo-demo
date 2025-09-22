# This program calculates the largest integer i such that the sum of
# the first i integers equals n or can be adjusted to equal n by 
# removing an even number from the sum.

# Read the integer input from the user and obtain its absolute value
n = abs(int(input()))

# Initialize the variable i to 0
i = 0

# Loop indefinitely until a break condition is encountered
while True:
    # Calculate the sum of the first i integers using the formula
    s = (i * (i + 1)) // 2  # Using integer division for compatibility
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
    
    # Increment i by 1 for the next iteration
    i += 1
