# Function to find the first non-negative integer based on the conditions provided
def find_first_non_negative_integer():
    # Initialize Input: Get a positive integer 'n' from the user
    n = abs(int(input()))  # Ensure we are working with an absolute integer
    
    # Set Initial Values
    index = 0
    
    # Repeat Until Found
    while True:
        # Calculate Sum
        sum_up_to_index = (index * (index + 1)) // 2  # Using integer division
        
        # Determine the Difference
        difference = sum_up_to_index - n
        
        # Check for Equality
        if sum_up_to_index == n:
            print(index)  # Print the current index
            break  # Exit the loop
        
        # Check for Greater Than Condition
        if sum_up_to_index > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the current index
                break  # Exit the loop
        
        # Increment Index
        index += 1  # Move to the next integer

# Call the function to execute
find_first_non_negative_integer()
