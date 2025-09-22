# Function to find the largest integer whose triangular number
# equals or exceeds the given absolute integer input
def find_triangular_integer():
    # Get user input and store the absolute value
    target_value = abs(int(input()))
    
    # Initialize counter for calculating triangular numbers
    counter = 0

    # Infinite loop to find the appropriate triangular number
    while True:
        # Calculate the triangular number
        triangular_number = (counter * (counter + 1)) // 2
        # Calculate the difference between the triangular number and the target value
        difference = triangular_number - target_value

        # Check if triangular number matches target value
        if triangular_number == target_value:
            print(counter)  # Output the counter value
            break  # Exit the loop

        # Check if triangular number exceeds target value
        elif triangular_number > target_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(counter)  # Output the counter value
                break  # Exit the loop

        # Increment counter for the next triangular number
        counter += 1

# Example usage:
# Uncomment the line below to run the function and test
# find_triangular_integer()
