def check_numbers_up_to(n):
    # Initialize a list to keep track of numbers, starting all as TRUE
    boolean_list = [True] * n
    
    # Initialize indices for tracking
    current_index = 0
    iteration_counter = 1
    
    # Start iterating up to a maximum of 500,000
    while iteration_counter <= 500000:
        # If the current index is marked as TRUE, mark it as FALSE
        if boolean_list[current_index]:
            boolean_list[current_index] = False
        
        # Move to the next index
        iteration_counter += 1
        current_index = (current_index + iteration_counter) % n
    
    # Filter the list to find all still TRUE values
    remaining_true_values = [value for value in boolean_list if value]
    
    # Check if there are any TRUE values left and print result
    if len(remaining_true_values) == 0:
        print('YES')
    else:
        print('NO')


# Read an integer input for n
n = int(input())
check_numbers_up_to(n)
