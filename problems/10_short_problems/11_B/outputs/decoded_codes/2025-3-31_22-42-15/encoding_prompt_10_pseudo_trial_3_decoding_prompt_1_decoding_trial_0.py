# Line 1: START
# Python does not have a 'START' or 'END' statement

# Line 2: DECLARE integer variable n
n = abs(int(input()))  # Line 3: SET n = absolute value of integer input

# Line 4: DECLARE integer variable i and initialize it to 0
i = 0

# Line 5: WHILE true DO
while True:
    # Line 6: SET variable s to (i * (i + 1)) / 2
    s = (i * (i + 1)) // 2  # Using integer division

    # Line 7: SET variable m to s - n
    m = s - n

    # Line 8: IF s equals n THEN
    if s == n:
        # Line 9: PRINT i
        print(i)  # Output the value of i if the sum equals n
        # Line 10: BREAK
        break  # Exit the loop
    
    # Line 11: ELSE IF s is greater than n THEN
    elif s > n:
        # Line 12: IF m is even THEN
        if m % 2 == 0:  # Check if m is even
            # Line 13: PRINT i
            print(i)  # Output the value of i if m is even
            # Line 14: BREAK
            break  # Exit the loop
    
    # Line 15: INCREMENT i by 1
    i += 1  # Move to the next integer

# Line 16 and 17: END WHILE and END are implied in Python, no action needed
