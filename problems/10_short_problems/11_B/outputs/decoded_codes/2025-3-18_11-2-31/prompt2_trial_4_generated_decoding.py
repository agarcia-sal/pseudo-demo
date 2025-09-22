# Step 1: Begin the program.

# Step 2: Prompt the user for an input number, ensuring it is a positive integer.
input_number = abs(int(input()))  # Reads input and takes absolute value to ensure positivity.

# Step 3: Set a counter variable named "current_index" to 0.
current_index = 0

# Step 4: Enter an infinite loop to perform calculations.
while True:
    # Step 4a: Calculate the sum of the first "current_index" integers.
    sum_of_indices = sum(range(current_index + 1))  # Sum of integers from 0 to current_index
    
    # Step 4b: Calculate the difference between "sum_of_indices" and the input number.
    difference = sum_of_indices - input_number
    
    # Step 4c: Check if "sum_of_indices" is equal to the input number.
    if sum_of_indices == input_number:
        print(current_index)  # Output the value of "current_index".
        break  # Exit the loop.
    
    # Step 4d: Otherwise, check if "sum_of_indices" is greater than the input number.
    if sum_of_indices > input_number:
        # Step 4d.i: Check if the "difference" is an even number.
        if difference % 2 == 0:  # Check if difference is even.
            print(current_index)  # Output the value of "current_index".
            break  # Exit the loop.
    
    # Step 4e: Increase the value of "current_index" by 1 to proceed to the next integer.
    current_index += 1

# Step 5: End the program. (Implicitly done when the program concludes.)
