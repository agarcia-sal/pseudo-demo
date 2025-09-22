# Function to find the smallest non-negative integer whose triangular number 
# either equals or exceeds a given absolute integer input, with conditions for the difference.
def find_smallest_triangular_index():
    # Get user input and take absolute value
    target_value = abs(int(input()))
    
    # Initialize an integer counter
    index = 0

    # Loop to find the desired triangular number
    while True:
        # Calculate the triangular number using the formula
        triangular_number = (index * (index + 1)) // 2
        
        # Compute the difference between the triangular number and the target value
        difference = triangular_number - target_value
        
        # Check if the triangular number equals the target value
        if triangular_number == target_value:
            print(index)  # Print the current value of index
            break  # Exit the loop
        # Check if the triangular number is greater than the target value
        elif triangular_number > target_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the current value of index
                break  # Exit the loop
        
        # Increment the index to check the next number in the next iteration
        index += 1

# Example Test Case: Input would have to be provided via the prompt.
# Invoke the function to execute
find_smallest_triangular_index()
