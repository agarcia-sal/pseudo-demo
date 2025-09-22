def check_prime_status():
    # Step 1: Input the number of elements
    n = int(input())
    
    # Step 2: Initialize a boolean list to track prime status
    is_prime = [True] * n

    # Step 3: Initialize variables for the iteration
    step = 1
    index = 0

    # Step 4: Loop to iterate a maximum of 500,000 times
    while step <= 500000:
        if is_prime[index]:  # Check if the current index position is True
            is_prime[index] = False  # Set it to False if it's True
        
        step += 1  # Increment the step
        index = (index + step) % n  # Move to the next position

    # Step 5: Collect remaining True values in a new list
    remaining_true = [value for value in is_prime if value]

    # Step 6: Check the result and output accordingly
    if not remaining_true:
        print("YES")
    else:
        print("NO")

# Test the function
check_prime_status()
