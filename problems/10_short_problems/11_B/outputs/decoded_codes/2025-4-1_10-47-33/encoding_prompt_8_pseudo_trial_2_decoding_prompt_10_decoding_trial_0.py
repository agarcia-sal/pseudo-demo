def find_smallest_integer_for_sum():
    # Step 1: Get input from the user and convert to absolute value
    number = abs(int(input()))
    
    # Step 2: Initialize a variable to keep track of the current integer
    current_integer = 0
    
    # Step 3: Enter an infinite loop to search for the desired integer
    while True:
        # Calculate the sum of the first 'current_integer' integers
        total_sum = (current_integer * (current_integer + 1)) // 2
        
        # Calculate the difference between 'total_sum' and 'number'
        difference = total_sum - number
        
        # Step 4: Check if the sum equals the user's number
        if total_sum == number:
            print(current_integer)  # Output the current integer
            break  # Exit the loop
        
        # Step 5: Check if total_sum is greater than the user's number
        elif total_sum > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_integer)  # Output the current integer
                break  # Exit the loop
        
        # Step 6: Increment the current integer for the next iteration
        current_integer += 1  # Move to the next integer

# Call the function to execute the program
find_smallest_integer_for_sum()
