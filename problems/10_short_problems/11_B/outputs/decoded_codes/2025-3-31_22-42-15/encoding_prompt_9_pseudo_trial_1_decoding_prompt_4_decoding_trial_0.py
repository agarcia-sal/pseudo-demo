# Function to find the least non-negative integer
def find_least_non_negative_integer():
    absolute_value = abs(int(input()))  # Get the absolute value of the input number
    index = 0  # Initialize index to 0 which will be used to calculate triangular numbers

    while True:  # Start an infinite loop
        # Calculate the triangular number using the formula
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference
        difference = triangular_number - absolute_value

        # Check for equality
        if triangular_number == absolute_value:
            print(index)  # Output the index
            break  # Exit the loop

        # Check for greater value
        if triangular_number > absolute_value:
            if difference % 2 == 0:  # Check if the difference is even
                print(index)  # Output the index
                break  # Exit the loop
        
        index += 1  # Increment index

# Call the function to execute the logic
find_least_non_negative_integer()
