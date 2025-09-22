# Function to determine if all elements can be marked as False
def process_boolean_list():
    # Read an integer input that defines the size of the list
    size_of_list = int(input())
    
    # Create a boolean list initialized to True for all indices
    boolean_list = [True] * size_of_list

    # Initialize index variables for processing
    current_index = 0
    iteration_counter = 1

    # Loop to process elements until a maximum of 500,000 iterations
    while iteration_counter <= 500000:
        # If the current position in the boolean list is still True,
        # mark it as False (indicating it has been processed)
        if boolean_list[current_index] is True:
            boolean_list[current_index] = False
        
        # Increment the iteration counter for the next step
        iteration_counter += 1
        
        # Calculate the next position using the current iteration counter
        current_index = (current_index + iteration_counter) % size_of_list
    
    # Create a new list containing all elements from boolean_list that are still True
    remaining_true = [element for element in boolean_list if element is True]

    # Check if there are any True values remaining in the list
    if len(remaining_true) == 0:
        # If no True values remain, output "YES"
        print("YES")
    else:
        # If there are still True values, output "NO"
        print("NO")

# Uncomment the line below to execute the function
# process_boolean_list()
