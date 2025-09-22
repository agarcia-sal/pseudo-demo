# Step 1: Initialize the variable n
n = abs(int(input()))

# Step 2: Set the variable i to 0
i = 0

# Step 3: Start an infinite loop
while True:
    # Calculate s as the sum of the first i natural numbers
    s = i * (i + 1) // 2
    
    # Calculate m as s - n
    m = s - n
    
    # Check if s is equal to n
    if s == n:
        print(i)
        break  # Exit the loop if true
    
    # Check if s is greater than n
    if s > n:
        # Check if m is an even number
        if m % 2 == 0:
            print(i)
            break  # Exit the loop if m is even

    # Increment the value of i by 1
    i += 1
