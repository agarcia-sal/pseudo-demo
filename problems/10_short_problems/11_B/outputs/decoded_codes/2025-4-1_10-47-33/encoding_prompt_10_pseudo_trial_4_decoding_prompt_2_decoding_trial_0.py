# Step 1: Initialize variable n as the absolute value of the integer input
n = abs(int(input()))

# Step 2: Set variable i to 0
i = 0

# Step 3: While true:
while True:
    # Step 4: Calculate the sum s as the sum of the first i integers
    s = i * (i + 1) // 2  # Integer division

    # Step 5: Calculate the difference m as s - n
    m = s - n

    # Step 6: If s is equal to n:
    if s == n:
        # Step 7: Print the value of i
        print(i)
        # Step 8: Terminate the loop
        break

    # Step 9: Else if s is greater than n:
    elif s > n:
        # Step 10: If m is even:
        if m % 2 == 0:
            # Step 11: Print the value of i
            print(i)
            # Step 12: Terminate the loop
            break

    # Step 13: Increment i by 1
    i += 1
