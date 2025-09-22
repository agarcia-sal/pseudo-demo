# Step 1: Initialize variable n to the absolute value of user input
n = abs(int(input()))

# Step 2: Initialize loop counter variable i
i = 0

# Start an infinite loop
while True:
    # Step 3: Calculate the sum of the first i natural numbers
    sum_i = (i * (i + 1)) // 2  # Using // for integer division

    # Step 4: Calculate the difference between sum_i and n
    difference = sum_i - n

    # Step 5: Check if sum_i matches n
    if sum_i == n:
        print(i)  # Output the value of i
        break  # Exit the loop

    # Step 6: Check if sum_i exceeds n
    if sum_i > n:
        # Step 7: Check if the difference is even
        if difference % 2 == 0:
            print(i)  # Output the value of i
            break  # Exit the loop

    # Step 8: Increment the loop counter
    i += 1
