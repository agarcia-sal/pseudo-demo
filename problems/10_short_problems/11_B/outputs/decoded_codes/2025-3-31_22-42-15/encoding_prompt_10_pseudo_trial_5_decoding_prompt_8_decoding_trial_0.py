# Step 1: Initialize variables
n = 0
i = 0

# Step 2: Get user input
n = abs(int(input()))

# Step 3: Infinite loop to find the solution
while True:
    # Step 4: Calculate the sum of the first i natural numbers
    s = (i * (i + 1)) // 2
    
    # Step 5: Calculate m as the difference between s and n
    m = s - n
    
    # Step 6: Check if the sum is equal to the input n
    if s == n:
        print(i)
        break  # Exit the loop

    # Step 7: Check if the sum exceeds the input n
    elif s > n:
        # Step 8: Check if the difference m is even
        if m % 2 == 0:
            print(i)
            break  # Exit the loop

    # Step 9: Increment i for the next iteration
    i += 1
