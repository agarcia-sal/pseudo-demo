# Step 1: Initialize variable n as the absolute value of the integer input
n = abs(int(input()))  # Read input and convert to absolute integer

# Step 2: Set variable i to 0
i = 0

# Step 3: Infinite loop to find the required value
while True:
    # Step 4: Calculate the sum s as the sum of the first i integers
    s = i * (i + 1) // 2  # Use integer division to calculate the sum

    # Step 5: Calculate the difference m as s - n
    m = s - n

    # Step 6: Check if s is equal to n
    if s == n:
        print(i)  # Step 7: Print the value of i
        break  # Step 8: Terminate the loop

    # Step 9: Else if s is greater than n
    elif s > n:
        # Step 10: Check if m is even
        if m % 2 == 0:  # Check if m is even
            print(i)  # Step 11: Print the value of i
            break  # Step 12: Terminate the loop

    # Step 13: Increment i by 1
    i += 1
