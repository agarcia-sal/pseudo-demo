# Function to find the smallest non-negative integer whose triangular number is equal to
# or exceeds a given target number, and checks if the difference is even if it exceeds.

def find_smallest_index():
    # Step 1: Receive and prepare input
    target_number = int(input())  # Convert input to a non-negative integer

    # Step 2: Initialize variables
    current_index = 0

    # Step 3: Process to find the desired index
    while True:
        # Calculate the triangular number
        triangular_number = (current_index * (current_index + 1)) // 2  # Using integer division
        
        # Calculate the difference
        difference = triangular_number - target_number

        # Check if triangular number equals target number
        if triangular_number == target_number:
            print(current_index)  # This is the answer
            break
        
        # Otherwise, check if triangular number is greater than target number
        if triangular_number > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_index)  # This is the answer
                break
        
        # Increment current index
        current_index += 1

# Call the function to execute.
find_smallest_index()
