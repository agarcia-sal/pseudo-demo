def main():
    # Receive input for the number of elements
    number_of_elements = int(input())

    # Initialize a list of boolean values indicating the status of each element
    status_list = [True] * number_of_elements

    # Initialize counters for the loop
    current_index = 0
    iteration_count = 1

    # Continue looping while the iteration_count is less than or equal to 500000
    while iteration_count <= 500000:
        # If the current element in the status_list is True
        if status_list[current_index]:
            # Mark the current element as False
            status_list[current_index] = False

        # Move to the next iteration count
        iteration_count += 1
        
        # Calculate the next index to modify in a circular manner
        current_index = (current_index + iteration_count) % number_of_elements

    # Create a new list containing only the True values from the status_list
    remaining_true_elements = [element for element in status_list if element]

    # Check if there are any True values left in the remaining_true_elements list
    if len(remaining_true_elements) == 0:
        # If no True values are found, output 'YES'
        print('YES')
    else:
        # If True values are found, output 'NO'
        print('NO')

# Run the main function
if __name__ == "__main__":
    main()
