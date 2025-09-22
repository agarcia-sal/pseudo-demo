def find_matching_index():
    # Step 1: Get user input and convert to absolute integer
    integer_value = abs(int(input()))
    
    # Step 2: Initialize a counter variable
    index = 0
    
    # Step 3: Create an infinite loop to find a solution
    while True:
        # Calculate the sum of the first 'index' natural numbers
        current_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between the calculated sum and the input value
        difference = current_sum - integer_value
        
        # Step 4: Check if the calculated sum matches the input value
        if current_sum == integer_value:
            print(index)
            break
        
        # Step 5: Check if the calculated sum exceeds the input value
        elif current_sum > integer_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# Running the function to execute the logic
find_matching_index()
