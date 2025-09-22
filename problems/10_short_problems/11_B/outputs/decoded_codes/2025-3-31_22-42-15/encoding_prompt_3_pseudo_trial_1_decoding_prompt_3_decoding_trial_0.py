# Function to calculate and print the index of the triangular number
def find_triangular_number_index():
    # Get the absolute value of the integer input from the user
    absolute_value = abs(int(input()))
    
    # Initialize a counter for triangular numbers
    index = 0

    # Infinite loop to calculate triangular numbers
    while True:
        # Calculate the triangular number for the current index
        triangular_number = (index * (index + 1)) // 2  # Using integer division
        
        # Calculate the difference between the triangular number and the user input
        difference = triangular_number - absolute_value
        
        # Check if the triangular number equals the user input
        if triangular_number == absolute_value:
            # If they are equal, print the current index
            print(index)
            # Exit the loop
            break
        
        # Check if the triangular number exceeds the user input
        elif triangular_number > absolute_value:
            # If the difference is even
            if difference % 2 == 0:
                # Print the current index
                print(index)
                # Exit the loop
                break
        
        # Increment the index to check the next triangular number
        index += 1

# Call the function to execute
find_triangular_number_index()
