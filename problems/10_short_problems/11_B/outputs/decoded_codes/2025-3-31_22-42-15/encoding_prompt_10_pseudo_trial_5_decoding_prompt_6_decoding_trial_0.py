# Step 1: Initialize variables
n = 0  # This will store the user input, which is a positive integer
i = 0  # This will be used to count the first i natural numbers

# Step 2: Get user input
n = abs(int(input()))  # Get the absolute value of an integer input from the user

# Step 3: Infinite loop to find the solution
while True:
    # Step 4: Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2  # Use integer division to calculate the sum

    # Step 5: Calculate m as the difference between s and n
    m = s - n  # Difference between sum and input number

    # Step 6: Check if the sum is equal to the input n
    if s == n:
        print(i)  # Output the current value of i
        break  # Exit the loop

    # Step 7: Check if the sum exceeds the input n
    elif s > n:
        # Step 8: Check if the difference m is even
        if m % 2 == 0:
            print(i)  # Output the current value of i
            break  # Exit the loop
    
    # Step 9: Increment i for the next iteration
    i += 1  # Increase i by 1 for the next loop iteration
