def find_index_for_sum():
    # Step 1: Read input
    n = int(input())  # Read input number
    n = abs(n)  # Take absolute value of n
    index = 0  # Initialize index

    # Step 2: Loop indefinitely to find the required value
    while True:
        # Calculate the sum of the first index natural numbers
        sum_n = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the input number
        difference = sum_n - n
        
        # Step 3: Check if the sum equals the input number
        if sum_n == n:
            print(index)  # Output the index when sum matches input number
            break  # Exit the loop
        
        # Step 4: Check if the sum exceeds the input number
        elif sum_n > n:
            # Step 5: Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index if the difference is even
                break  # Exit the loop
        
        # Step 6: Increment index for the next iteration
        index += 1

# Call the function
find_index_for_sum()
