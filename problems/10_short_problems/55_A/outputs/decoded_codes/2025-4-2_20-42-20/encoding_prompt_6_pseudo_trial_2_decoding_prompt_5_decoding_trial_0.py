# Python code to implement the logic from the provided pseudocode

def process_boolean_array():
    # Read an integer input representing the size of the array
    size_of_array = int(input())
    
    # Initialize a boolean array with size_of_array elements, all set to True
    boolean_array = [True] * size_of_array
    
    # Initialize two variables for tracking the current state
    index_to_update = 0
    step_count = 1
    
    # Continue the loop while step_count is less than or equal to 500,000
    while step_count <= 500000:
        # Check if the current position in the boolean array is True
        if boolean_array[index_to_update]:
            # Set the current position to False, indicating it has been processed
            boolean_array[index_to_update] = False
        
        # Increment the step count
        step_count += 1
        
        # Update the index to the next position in the array using modulo operation
        index_to_update = (index_to_update + step_count) % size_of_array
    
    # Create a new list that contains all elements from boolean_array that are still True
    filtered_list = [element for element in boolean_array if element]
    
    # Check if the filtered list is empty
    if len(filtered_list) == 0:
        # If the filtered list is empty, output "YES"
        print("YES")
    else:
        # If the filtered list is not empty, output "NO"
        print("NO")

# Execute the function
process_boolean_array()
