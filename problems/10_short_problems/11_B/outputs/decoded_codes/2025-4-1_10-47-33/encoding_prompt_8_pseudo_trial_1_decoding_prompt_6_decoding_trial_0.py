# Step 1: Get input from the user and convert it to a non-negative integer
target_number = int(input())

# Step 2: Initialize the current integer
current_integer = 0

# Step 3: Start an endless loop to find the result
while True:
    # Calculate the sum of all integers from 0 to current_integer
    sum_of_integers = (current_integer * (current_integer + 1)) // 2  # Using the formula for the sum of the first n integers

    # Calculate the difference between sum_of_integers and target_number
    difference = sum_of_integers - target_number
    
    # Check conditions
    if sum_of_integers == target_number: 
        # If the sum matches the target number, print current_integer
        print(current_integer)
        break  # Exit the loop

    elif sum_of_integers > target_number:
        # If the sum exceeds the target number, check if the difference is even
        if difference % 2 == 0:
            # If the difference is even, print current_integer
            print(current_integer)
            break  # Exit the loop

    # Increase current_integer to check the next integer in the next iteration
    current_integer += 1
