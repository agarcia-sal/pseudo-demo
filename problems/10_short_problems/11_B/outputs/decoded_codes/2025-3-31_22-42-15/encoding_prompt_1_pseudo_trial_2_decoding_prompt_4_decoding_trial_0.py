def find_integer_sum():
    # Step 2: Input the absolute value of an integer
    n = abs(int(input()))
    
    # Step 3: Initialize index variable
    i = 0
    
    # Step 4: Loop indefinitely
    while True:
        # Step 1: Calculate the sum of the first `i` integers
        s = (i * (i + 1)) // 2  # Using integer division
        
        # Step 2: Calculate the difference between the sum and `n`
        m = s - n
        
        # Step 3: Check if the sum equals `n`
        if s == n:
            print(i)
            break  # Exit the loop
        
        # Step 4: Check if the sum is greater than `n`
        if s > n:
            # Step 5: Check if the difference `m` is even
            if m % 2 == 0:
                print(i)
                break  # Exit the loop
        
        # Step 6: Increment the index variable
        i += 1

# Calling the function to execute the logic
find_integer_sum()
