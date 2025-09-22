def find_non_negative_integer():
    # Step 1: Accept an input value
    input_value = abs(int(input()))  # Using absolute value to handle negative inputs
    index = 0
    
    # Step 2: Start an infinite loop to find the correct index
    while True:
        # Step 3: Calculate the sum of the first 'index' natural numbers
        sum_value = (index * (index + 1)) // 2  # Using integer division
        
        # Step 4: Calculate the difference between the sum and input value
        difference = sum_value - input_value
        
        # Step 5: Check if the sum equals the input value
        if sum_value == input_value:
            # Step 5a: If they are equal, print the current index
            print(index)
            break
        
        # Step 6: Check if the sum is greater than the input value
        elif sum_value > input_value:
            # Step 6a: Check if the difference is even
            if difference % 2 == 0:
                # Step 6b: If the difference is even, print the current index
                print(index)
                break
        
        # Step 7: Move to the next index for the next iteration
        index += 1

# Call the function to run the code
find_non_negative_integer()
