# Step 1: START

# Step 2: DECLARE integer variable n
n = abs(int(input()))  # Step 3: SET n = absolute value of integer input
# Step 4: DECLARE integer variable i and initialize it to 0
i = 0

# Step 5: WHILE true DO
while True:
    # Step 6: SET variable s to (i * (i + 1)) / 2
    s = (i * (i + 1)) // 2  # Using // for integer division
    # Step 7: SET variable m to s - n
    m = s - n  

    # Step 8: IF s equals n THEN
    if s == n:
        # Step 9: PRINT i
        print(i)  # Output the value of i if the sum equals n
        # Step 10: BREAK
        break  # Exit the loop

    # Step 11: ELSE IF s is greater than n THEN
    elif s > n:
        # Step 12: IF m is even THEN
        if m % 2 == 0:
            # Step 13: PRINT i
            print(i)  # Output the value of i if m is even
            # Step 14: BREAK
            break  # Exit the loop

    # Step 15: INCREMENT i by 1
    i += 1  # Move to the next integer

# Step 16: END WHILE

# Step 17: END
