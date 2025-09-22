def find_index():
    # Step 1: Get absolute value of user input and convert to integer
    input_value = abs(int(input()))
    
    # Step 2: Initialize an index variable
    index = 0

    # Step 3: Loop indefinitely to find a solution
    while True:
        # Calculate the sum of the first "index" natural numbers
        current_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the input value
        difference = current_sum - input_value
        
        # Step 4: Check if the computed sum is equal to the input value
        if current_sum == input_value:
            print(index)
            break
        
        # Step 5: Check if the computed sum exceeds the input value
        elif current_sum > input_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index for the next iteration
        index += 1

# Call the function to execute
find_index()
