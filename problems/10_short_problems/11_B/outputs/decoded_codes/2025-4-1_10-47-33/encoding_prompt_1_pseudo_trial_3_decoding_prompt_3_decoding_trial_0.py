def find_integer_sequence():
    # Step 1: Initialize the variable n to the absolute value of the integer input
    n = abs(int(input()))
    
    # Step 2: Set the variable i to 0
    i = 0
    
    # Step 3: Start an infinite loop to perform actions
    while True:
        # Calculate the sum of the first i natural numbers
        s = i * (i + 1) // 2  # Using integer division for clarity
        
        # Calculate m as the difference between the sum and n
        m = s - n
        
        # Check if s is equal to n
        if s == n:
            print(i)
            break  # Exit the loop if condition is met
            
        # Check if s is greater than n
        if s > n:
            # Check if m is an even number
            if m % 2 == 0:
                print(i)
                break  # Exit the loop if condition is met
                
        # Increment i to check the next number in the sequence
        i += 1

# Calling the function to execute
find_integer_sequence()
