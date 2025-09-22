def calculate_smallest_integer():
    # Step 1: Get input and convert it to an absolute integer
    user_input = int(input())
    absolute_input = abs(user_input)

    # Step 2: Initialize the counter variable
    current_integer = 0

    # Step 3: Loop for Triangular Numbers
    while True:
        # Calculate the triangular number for current_integer
        triangular_number = (current_integer * (current_integer + 1)) // 2
        
        # Calculate the difference between triangular_number and absolute_input
        difference = triangular_number - absolute_input
        
        # Check the conditions
        if triangular_number == absolute_input:
            # Case where the triangular number exactly equals absolute input
            print(current_integer)
            break
        elif triangular_number > absolute_input:
            if difference % 2 == 0:
                # Case where the triangular number exceeds absolute input with an even difference
                print(current_integer)
                break
        
        # Increment current_integer to check the next number
        current_integer += 1

# Call the function to execute the code
calculate_smallest_integer()
