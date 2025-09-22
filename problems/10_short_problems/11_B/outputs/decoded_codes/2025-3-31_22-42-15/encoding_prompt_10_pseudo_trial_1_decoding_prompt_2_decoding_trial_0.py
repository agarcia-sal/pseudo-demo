# Step 1: Start

# Step 2: Declare Variables
n = abs(int(input()))  # Set variable `n` to the absolute value of the integer input
i = 0  # Set variable `i` to 0 

# Step 3: Begin Infinite Loop
while True:
    # Compute the triangular number `s`
    s = (i * (i + 1)) / 2  # `s` = (i * (i + 1)) / 2
    m = s - n  # Set variable `m` to `s - n`

    # Step 4: Check Conditions
    if s == n:  # If `s` equals `n`
        print(i)  # Display the value of `i`
        break  # Exit the loop
    elif s > n:  # Else If `s` is greater than `n`
        if m % 2 == 0:  # If `m` is an even number
            print(i)  # Display the value of `i`
            break  # Exit the loop

    # Step 5: Increment `i` by 1
    i += 1  # Increment `i` by 1

# Step 6: Repeat from Step 3
# This is managed by the while loop

# Step 7: End
