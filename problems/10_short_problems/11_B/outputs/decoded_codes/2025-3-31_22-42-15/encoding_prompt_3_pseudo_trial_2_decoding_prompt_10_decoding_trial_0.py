def find_index_for_input_number():
    # Step 1: Get user input and calculate the absolute value
    input_number = abs(int(input()))  # Convert input to integer and take absolute value

    # Step 2: Initialize loop variable
    index = 0

    # Step 3: Begin an infinite loop to find the solution
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_natural_numbers = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and input_number
        difference = sum_natural_numbers - input_number

        # Step 4: Check if the current sum equals the input number
        if sum_natural_numbers == input_number:
            print(index)
            break

        # Step 5: Check if the current sum exceeds the input number
        elif sum_natural_numbers > input_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break

        # Increment the loop variable
        index += 1

# Call the function to execute the process
find_index_for_input_number()
