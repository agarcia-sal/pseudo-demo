# Step 1: Initialize the variable
n = abs(int(input()))  # Taking the absolute value of the integer input
i = 0  # Setting the iterator to 0

# Step 2: Start an infinite loop to calculate triangular numbers
while True:
    # Step 3: Calculate the triangular number for the current i
    s = (i * (i + 1)) // 2  # Calculation of the triangular number using integer division

    # Step 4: Calculate the difference between the triangular number and n
    m = s - n

    # Step 5: Check if the triangular number equals n
    if s == n:
        print(i)
        break  # Exit the loop

    # Step 6: Check if the triangular number exceeds n
    elif s > n:
        # Step 7: Check if the difference is even
        if m % 2 == 0:
            print(i)
            break  # Exit the loop

    # Step 8: Increment i for the next iteration
    i += 1
