# Step 1: Input
n = abs(int(input()))

# Step 2: Initialization
i = 0

# Step 3: Looping Process
while True:
    # Calculate sum of the first i integers
    s = (i * (i + 1)) / 2
    
    # Determine the difference
    m = s - n
    
    # Check conditions
    if s == n:
        print(i)
        break
    elif s > n:
        if m % 2 == 0:
            print(i)
            break
    
    # Increment the counter
    i += 1
