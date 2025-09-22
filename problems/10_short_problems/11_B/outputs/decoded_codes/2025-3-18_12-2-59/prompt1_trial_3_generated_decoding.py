# Step 1: Input
n = int(input())
n = abs(n)  # Taking the absolute value

# Step 2: Initialize the counter
i = 0

# Step 3: Loop
while True:
    # Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2
    
    # Calculate the difference
    m = s - n
    
    # Check Conditions
    if s == n:
        print(i)
        break
    elif s > n:
        if m % 2 == 0:  # Check if m is even
            print(i)
            break

    # Increment the counter
    i += 1
