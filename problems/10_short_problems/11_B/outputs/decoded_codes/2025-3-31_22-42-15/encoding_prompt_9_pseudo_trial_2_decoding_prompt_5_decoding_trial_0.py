# This function finds the smallest non-negative integer such that either 
# its corresponding triangular number is equal to a specified input 
# or can be adjusted to match the input by removing an even number.

def find_smallest_integer():
    # Get the absolute value of input from the user
    target_number = abs(int(input()))
    
    # Initialize the current integer to evaluate
    current_integer = 0
    
    while True:
        # Calculate the triangular number for current_integer
        triangular_number = (current_integer * (current_integer + 1)) / 2
        
        # Calculate the difference between the triangular number and target number
        difference = triangular_number - target_number
        
        # Check if triangular_number is equal to target_number
        if triangular_number == target_number:
            print(current_integer)  # Output the current integer
            break  # Exit the loop
        
        # Check if triangular_number is greater than target_number
        elif triangular_number > target_number:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(current_integer)  # Output the current integer
                break  # Exit the loop
        
        # Increment the integer for the next iteration
        current_integer += 1

# Function can be tested by calling it, user will provide input when run
# find_smallest_integer()
