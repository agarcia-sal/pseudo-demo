def find_target_index():
    # Step 1: Get the absolute value of user input and convert it to an integer
    target_value = abs(int(input()))

    # Step 2: Initialize a counter variable to keep track of the current iteration
    index = 0

    # Step 3: Begin an infinite loop to compute values until a condition is met
    while True:
        # Step 4: Calculate the sum of the first 'index' natural numbers
        sum_value = (index * (index + 1)) // 2
        
        # Step 5: Calculate the difference between the current sum and the target value
        difference = sum_value - target_value
        
        # Step 6: Check if the current sum matches the target value
        if sum_value == target_value:
            print(index)  # Output the current index
            break  # Exit the loop

        # Step 7: Check if the current sum exceeds the target value
        elif sum_value > target_value:
            # Step 8: Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the current index
                break  # Exit the loop
        
        # Step 9: Increment the index to explore the next number
        index += 1

# Invoke the function to start the program
find_target_index()
