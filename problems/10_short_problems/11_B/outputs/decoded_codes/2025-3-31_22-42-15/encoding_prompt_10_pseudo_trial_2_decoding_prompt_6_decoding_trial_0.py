# Step 1: Initialize the variable n from user input and take its absolute value
n = abs(int(input()))

# Step 2: Start an infinite loop to calculate triangular numbers
i = 0

while True:
    # Step 3: Calculate the triangular number for the current i
    triangular_number = (i * (i + 1)) // 2  # Using integer division

    # Step 4: Calculate the difference between the triangular number and n
    difference = triangular_number - n

    # Step 5: Check if the triangular number equals n
    if triangular_number == n:
        print(i)  # Output the current value of i
        break

    # Step 6: Check if the triangular number exceeds n
    elif triangular_number > n:
        # Step 7: Check if the difference is even
        if difference % 2 == 0:
            print(i)  # Output the current value of i
            break

    # Step 8: Increment i for the next iteration
    i += 1
