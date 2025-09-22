def find_smallest_integer():
    # Step 1: Get input from the user and take its absolute value
    number = abs(int(input()))
    
    # Step 2: Initialize a variable to keep track of the current integer
    current_integer = 0

    # Step 3: Enter an infinite loop to search for the desired integer
    while True:
        # Calculate the sum of the first 'current_integer' integers
        sum_of_integers = (current_integer * (current_integer + 1)) // 2
        
        # Calculate the difference between 'sum_of_integers' and 'number'
        difference = sum_of_integers - number
        
        # Step 4: Check if the sum equals the user's number
        if sum_of_integers == number:
            print(current_integer)  # Output the current integer
            break  # Exit the loop

        # Step 5: Check if sum is greater than the user's number
        elif sum_of_integers > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_integer)  # Output the current integer
                break  # Exit the loop

        # Step 6: Increment the current integer for the next iteration
        current_integer += 1  # Move to the next integer

# Call the function to execute
find_smallest_integer()
