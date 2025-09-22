def find_integer(n):
    # Step 1: Initialize variables
    n = abs(int(n))  # Absolute value of the input integer
    i = 0  # Initialize the counter

    # Step 2: Start infinite loop
    while True:
        # Step 3: Calculate the sum of the first i integers
        sum_i = (i * (i + 1)) // 2  # Using integer division
        
        # Step 4: Calculate the difference
        difference = sum_i - n
        
        # Step 5: Check if the sum equals n
        if sum_i == n:
            print(i)
            break  # Exit the loop
        
        # Step 6: Check if the sum exceeds n
        elif sum_i > n:
            if difference % 2 == 0:  # Check if the difference is even
                print(i)
                break  # Exit the loop
        
        # Step 7: Increment i by 1
        i += 1

# Read input from user
input_value = input()
find_integer(input_value)
