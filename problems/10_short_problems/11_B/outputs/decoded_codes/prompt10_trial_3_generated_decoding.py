def find_smallest_index():
    # Step 1: Get an integer input and take its absolute value.
    n = abs(int(input()))
    i = 0

    # Step 2: Start an infinite loop until we break out of it.
    while True:
        # Step 3a: Calculate the sum of the first i natural numbers.
        sum_natural_numbers = (i * (i + 1)) // 2  # Using integer division

        # Step 3b: Calculate the difference between the sum and n.
        difference = sum_natural_numbers - n
        
        # Step 3c: Check conditions.
        if sum_natural_numbers == n:
            print(i)
            break  # Exit the loop
        
        elif sum_natural_numbers > n:
            if difference % 2 == 0:  # Check if difference is even
                print(i)
                break  # Exit the loop
        
        # Step 3d: Increment the counter.
        i += 1

# Call the function to execute.
find_smallest_index()
