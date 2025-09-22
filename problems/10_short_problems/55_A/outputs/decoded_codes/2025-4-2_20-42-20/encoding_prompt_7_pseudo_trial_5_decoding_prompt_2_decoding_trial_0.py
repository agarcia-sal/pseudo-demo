def check_remaining_true_values(input_number):
    # Convert the input into an integer
    total_elements = input_number

    # Initialize an array of boolean values all set to True
    boolean_array = [True] * total_elements

    # Initialize index variables
    current_index = 0
    step_counter = 1

    # Loop while step_counter is less than or equal to 500000
    while step_counter <= 500000:
        # Check if the current index has a True value
        if boolean_array[current_index]:
            # Set the value at the current index to False
            boolean_array[current_index] = False
        
        # Increment step_counter
        step_counter += 1

        # Calculate the new index using the step_counter
        current_index = (current_index + step_counter) % total_elements

    # Create a list of all True values remaining in the boolean array
    remaining_true_values = [value for value in boolean_array if value]

    # Check if there are any True values remaining
    if len(remaining_true_values) == 0:
        print('YES')
    else:
        print('NO')

# Example of how to call the function (without input parameters)
input_number = int(input())
check_remaining_true_values(input_number)
