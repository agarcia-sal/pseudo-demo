def find_triangular_number():
    # Step 1: Input absolute value of the number
    number = abs(int(input()))
    
    # Step 2: Initialize the counter variable
    index = 0
    
    # Step 3: Loop indefinitely to find the triangular number
    while True:
        # Step 3a: Calculate the triangular number
        triangular_sum = (index * (index + 1)) // 2
        
        # Step 3b: Calculate the difference from the input number
        difference = triangular_sum - number
        
        # Step 3c: Check conditions
        if triangular_sum == number:
            print(index)
            break  # Exit loop if it is a triangular number
        elif triangular_sum > number:
            if difference % 2 == 0:
                print(index)
                break  # Exit loop if number can be represented as a triangular number with an adjustment
        
        # Step 3d: Increment counter
        index += 1

# Call the function to execute
find_triangular_number()
