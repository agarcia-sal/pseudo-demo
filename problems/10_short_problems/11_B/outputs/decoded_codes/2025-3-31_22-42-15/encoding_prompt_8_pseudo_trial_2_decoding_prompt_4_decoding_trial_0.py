def find_smallest_integer():
    # Step 1: Get Input
    user_input = int(input())
    absolute_input = abs(user_input)

    # Step 2: Initialize Variables
    current_integer = 0

    # Step 3: Loop for Triangular Numbers
    while True:
        # Calculate the triangular number
        triangular_number = (current_integer * (current_integer + 1)) // 2
        
        # Calculate the difference
        difference = triangular_number - absolute_input

        # Check Conditions
        if triangular_number == absolute_input:
            print(current_integer)
            break
        elif triangular_number > absolute_input:
            if difference % 2 == 0:
                print(current_integer)
                break
        
        # Increment current_integer
        current_integer += 1

# Call the function to execute
find_smallest_integer()
