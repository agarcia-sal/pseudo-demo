def find_triangular_number():
    # Step 1: Input - Get absolute value of user input
    number = abs(int(input()))
    
    # Step 2: Initialize - Start counter variable
    index = 0
    
    # Step 3: Loop indefinitely
    while True:
        # Step 3a: Calculate Triangular Number
        triangular_sum = (index * (index + 1)) // 2
        
        # Step 3b: Calculate Difference
        difference = triangular_sum - number
        
        # Step 3c: Check Conditions
        if triangular_sum == number:
            print(index)  # Number is a triangular number
            break
        elif triangular_sum > number:
            if difference % 2 == 0:
                print(index)  # Number can be represented as a triangular number with an adjustment
                break
        
        # Step 3d: Increment Counter
        index += 1

# To run the function, simply call it
find_triangular_number()
