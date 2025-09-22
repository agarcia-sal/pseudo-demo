# Step 1: Initialize n to the absolute value of the integer input from the user.
n = abs(int(input()))

# Step 2: Initialize the counter i to 0.
i = 0

# Step 3: Repeat indefinitely (loop):
while True:
    # Calculate the sum s which is the sum of the first i natural numbers.
    s = i * (i + 1) // 2  # using integer division for consistency
    
    # Calculate the difference m as s - n.
    m = s - n
    
    # Check if the sum s is equal to n.
    if s == n:
        # Output the value of i.
        print(i)
        # Exit the loop.
        break
    # Check if the sum s is greater than n.
    elif s > n:
        # Check if the difference m is even.
        if m % 2 == 0:
            # Output the value of i.
            print(i)
            # Exit the loop.
            break
            
    # Increment the counter i by 1.
    i += 1
