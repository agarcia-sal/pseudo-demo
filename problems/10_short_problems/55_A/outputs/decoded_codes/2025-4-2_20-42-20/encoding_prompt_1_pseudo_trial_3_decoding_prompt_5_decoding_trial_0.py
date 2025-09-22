# Function to perform the algorithm as described in the pseudocode
def check_remaining_elements():
    # Input: Read an integer value n
    n = int(input())
    
    # Initialize
    is_true = [True] * n  # Create a list filled with True values
    current_index = 0     # Initialize current index
    step = 1              # Initialize step

    # Loop until step exceeds 500,000
    while step <= 500000:
        # Check if the value at currentIndex in isTrue is True
        if is_true[current_index]:
            is_true[current_index] = False  # Set that position to False
        
        # Increment step by 1
        step += 1
        
        # Update currentIndex using the formula
        current_index = (current_index + step) % n

    # Filter: Create a new list with the remaining True values
    remaining_true = [value for value in is_true if value]

    # Check outcome and output result
    if len(remaining_true) == 0:
        print("YES")
    else:
        print("NO")

# Example test case (uncomment the line below to test)
# check_remaining_elements()  # Run the function to see the output
