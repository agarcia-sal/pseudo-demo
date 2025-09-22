# Function to find the index of the triangular number that meets certain conditions
def find_triangular_number_index():
    # Read an integer from user input and store its absolute value
    target_value = abs(int(input()))

    # Initialize index counter
    index = 0

    # Infinite loop
    while True:
        # Calculate the triangular number using the formula
        triangular_number = (index * (index + 1)) / 2
        
        # Calculate the difference
        difference = triangular_number - target_value
        
        # Check conditions
        if triangular_number == target_value:
            print(index)  # Print index if triangular number equals target value
            break
        elif triangular_number > target_value:
            if difference % 2 == 0:  # Check if difference is even
                print(index)  # Print index if difference is even
                break
        
        # Increment index counter
        index += 1

# Call the function to execute
find_triangular_number_index()
