# Function to find the smallest non-negative integer based on the algorithm described
def find_smallest_integer():
    # Get the target number from user input and convert it to an absolute integer
    target_number = abs(int(input()))
    
    # Initialize the current integer to 0
    current_integer = 0
    
    # Start an infinite loop to find the required integer
    while True:
        # Calculate the sum of all integers from 0 to current_integer
        sum_of_integers = (current_integer * (current_integer + 1)) // 2
        
        # Calculate the difference between the sum and the target number
        difference = sum_of_integers - target_number
        
        # Check if the sum is equal to the target number
        if sum_of_integers == target_number:
            print(current_integer)  # Output current_integer and exit
            break
        
        # Check if the sum exceeds the target number
        if sum_of_integers > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_integer)  # Output current_integer and exit
                break
        
        # Increment current_integer for the next iteration
        current_integer += 1

# Example usage, the function can be called without parameters
find_smallest_integer()
