# Step 1: Initialize the variable
n = abs(int(input()))  # input for integer, take absolute value
i = 0  # Step 1: Initialize iterator

# Step 2: Start an infinite loop to calculate triangular numbers
while True:  # Step 2: Infinite loop
    # Step 3: Calculate the triangular number for the current i
    s = (i * (i + 1)) // 2  # Step 3: Calculate triangular number

    # Step 4: Calculate the difference between the triangular number and n
    m = s - n  # Step 4: Calculate the difference

    # Step 5: Check if the triangular number equals n
    if s == n:  # Step 5: Check for exact match
        print(i)  # Step 5: Output the result
        break  # Exit the loop

    # Step 6: Check if the triangular number exceeds n
    elif s > n:  # Step 6: Check if s is greater than n
        # Step 7: Check if the difference is even
        if m % 2 == 0:  # Step 7: Check if difference is even
            print(i)  # Step 7: Output the result
            break  # Exit the loop

    # Step 8: Increment i for the next iteration
    i += 1  # Step 8: Increment the iterator
