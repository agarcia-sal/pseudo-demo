# Step 1: Read Input
n = abs(int(input()))

# Step 2: Initialize Variables
i = 0

# Step 3: Start Infinite Loop
while True:
    # Step 3a: Calculate Sum
    s = (i * (i + 1)) // 2  # Using integer division to match the pseudocode

    # Step 3b: Calculate Difference
    m = s - n
    
    # Step 3c: Check Conditions
    if s == n:
        print(i)
        break
    elif s > n:
        if m % 2 == 0:  # Check if m is an even number
            print(i)
            break

    # Step 3d: Increment Counter
    i += 1
