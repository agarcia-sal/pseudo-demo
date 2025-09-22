def find_index():
    # Step 1: Get user input and convert it to a positive integer
    input_number = abs(int(input()))

    # Step 2: Initialize loop variable
    index = 0

    # Step 3: Begin an infinite loop to find the solution
    while True:
        # Calculate the sum of the first 'index' natural numbers
        current_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and input_number
        difference = current_sum - input_number

        # Step 4: Check if the current sum equals the input number
        if current_sum == input_number:
            print(index)
            break

        # Step 5: Check if the current sum exceeds the input number
        elif current_sum > input_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the loop variable
        index += 1

# Testing the function
find_index()
