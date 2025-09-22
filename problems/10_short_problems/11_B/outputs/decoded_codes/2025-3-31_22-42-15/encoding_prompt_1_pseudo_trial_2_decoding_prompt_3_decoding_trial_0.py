def find_integer():
    # Step 2: Input the absolute value of an integer
    n = abs(int(input()))  # Read the integer input and take the absolute value
    
    # Step 3: Initialize index variable
    i = 0  # Start with the first integer

    # Step 4: Loop indefinitely
    while True:
        # Step 4.1: Calculate the sum of the first `i` integers
        s = (i * (i + 1)) // 2  # Using integer division for clarity and to ensure an integer result
        
        # Step 4.2: Calculate the difference between the sum and `n`
        m = s - n
        
        # Step 4.3: Check if the sum equals `n`
        if s == n:
            print(i)  # Print the value of `i` when the sum equals `n`
            break
        
        # Step 4.4: Check if the sum is greater than `n`
        if s > n:
            # Step 4.4.1: Check if the difference `m` is even
            if m % 2 == 0:  # Check if `m` is even
                print(i)  # Print the value of `i` when `m` is even
                break
        
        # Step 4.5: Increment the index variable
        i += 1  # Increase `i` by 1 for the next iteration

# To run the function
find_integer()
