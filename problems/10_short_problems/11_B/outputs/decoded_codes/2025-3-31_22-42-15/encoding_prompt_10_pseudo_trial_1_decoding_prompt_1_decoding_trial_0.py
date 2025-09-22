# Step 1: Start

# Step 2: Declare Variables
n = abs(int(input()))  # Taking absolute value of the integer input
i = 0                  # Initializing counter variable

# Step 3: Begin Infinite Loop
while True:
    # Compute the triangular number s
    s = (i * (i + 1)) // 2  # Using integer division for triangular number
    m = s - n               # Calculate the difference

    # Step 4: Check Conditions
    if s == n:
        print(i)            # Display the value of i
        break               # Exit the loop
    elif s > n:
        if m % 2 == 0:      # Check if m is even
            print(i)        # Display the value of i
            break           # Exit the loop

    # Step 5: Increment i by 1
    i += 1

# Step 6: (Implicit in control structure, loop repeats)
# Step 7: End
