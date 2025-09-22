# Define the function to find the index of the triangular number
def find_triangular_number_index():
    # Read user input and convert it to a non-negative integer
    target_number = abs(int(input()))
    
    # Initialize a counter for the current index
    index = 0
    
    # Infinite loop to calculate triangular numbers
    while True:
        # Calculate the triangular number using the formula
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference between the triangular number and the target number
        difference = triangular_number - target_number
        
        # Check if the triangular number equals the target number
        if triangular_number == target_number:
            print(index)  # Print the index and exit the loop
            break
        # Check if the triangular number is greater than the target number
        elif triangular_number > target_number:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(index)  # Print the index and exit the loop
                break
        
        # Increment the index for the next triangular number
        index += 1

# Call the function to execute
find_triangular_number_index()
