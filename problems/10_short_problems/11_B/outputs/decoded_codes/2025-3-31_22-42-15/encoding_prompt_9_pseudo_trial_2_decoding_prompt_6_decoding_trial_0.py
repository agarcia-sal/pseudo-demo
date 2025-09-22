# Step 1: Receive the input and convert it to an absolute integer
target_number = abs(int(input()))  # Get a number from the user

# Step 2: Initialize variables
current_integer = 0  # This will keep track of the current number being evaluated

# Step 3: Start an infinite loop to find the valid number
while True:
    # Step 4: Calculate the triangular number
    triangular_number = (current_integer * (current_integer + 1)) / 2
    
    # Step 5: Determine the difference
    difference = triangular_number - target_number
    
    # Step 6: Check conditions
    if triangular_number == target_number:
        print(current_integer)  # Output the current integer if it matches
        break  # Exit the loop, valid number found
    elif triangular_number > target_number:
        if difference % 2 == 0:  # Check if the difference is even
            print(current_integer)  # Output the current integer if adjustment can match
            break  # Exit the loop, valid adjustment found
    
    # Step 7: Increment the integer
    current_integer += 1
