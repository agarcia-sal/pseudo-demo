# Function to find the smallest non-negative integer such that the sum of all integers from 0 to that integer
# equals a target number or can be adjusted to equal the target number by an even difference.

# Get input from the user
target_number = int(input())  # Read input and convert it to a non-negative integer

# Initialize the current integer to 0
current_integer = 0

# Endless loop to find the result
while True:
    # Calculate the sum of integers from 0 to current_integer
    sum_of_integers = (current_integer * (current_integer + 1)) // 2
    
    # Calculate the difference from the target
    difference = sum_of_integers - target_number
    
    # Check the conditions for equality and potential even difference
    if sum_of_integers == target_number:
        print(current_integer)  # Found the solution
        break  # Exit the loop
    elif sum_of_integers > target_number:
        if difference % 2 == 0:  # Check if the difference is even
            print(current_integer)  # Found the solution
            break  # Exit the loop
            
    # Increment current_integer for the next iteration
    current_integer += 1
