# Function to find the smallest non-negative integer
def find_smallest_integer():
    # Step 1: Get Input
    target_number = int(input())  # Read input as a non-negative integer

    # Step 2: Initialize current integer
    current_integer = 0

    # Step 3: Loop to find the result
    while True:
        # Calculate the sum of integers from 0 to current_integer
        sum_of_integers = (current_integer * (current_integer + 1)) // 2
        
        # Calculate the difference from the target number
        difference = sum_of_integers - target_number
        
        # Check conditions
        if sum_of_integers == target_number:
            print(current_integer)  # Print the current integer
            break
        elif sum_of_integers > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_integer)  # Print the current integer
                break
        
        # Increase current_integer for next iteration
        current_integer += 1

# Call the function to execute
find_smallest_integer()
