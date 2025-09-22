# Function to find the smallest integer whose triangular number
# is equal to or exceeds the absolute value of the input
def find_smallest_integer():
    # Get user input and convert it to absolute integer
    user_input = int(input())
    absolute_input = abs(user_input)

    # Initialize the counter for current integer
    current_integer = 0

    # Loop to find the appropriate triangular number
    while True:
        # Calculate the triangular number for the current integer
        triangular_number = (current_integer * (current_integer + 1)) // 2
        
        # Calculate the difference between triangular number and absolute input
        difference = triangular_number - absolute_input

        # Check for conditions to display the current integer and stop the loop
        if triangular_number == absolute_input:
            print(current_integer)
            break
        elif triangular_number > absolute_input:
            if difference % 2 == 0:  # Check if the difference is even
                print(current_integer)
                break
        
        # Increment the current integer for the next iteration
        current_integer += 1

# Call the function to execute
find_smallest_integer()
