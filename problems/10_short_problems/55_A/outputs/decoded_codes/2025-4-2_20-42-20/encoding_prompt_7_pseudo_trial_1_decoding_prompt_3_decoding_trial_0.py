def check_if_all_positions_are_false(n):
    # Create a list of boolean values initialized to True
    boolean_list = [True] * n

    # Initialize necessary indices
    index = 0
    step = 1

    # Loop until the step exceeds 500,000
    while step <= 500000:
        # If the current index in the boolean list is True
        if boolean_list[index]:
            # Set the current position to False
            boolean_list[index] = False
        
        # Move to the next step
        step += 1
        
        # Calculate the next index based on current index and step size
        index = (index + step) % n

    # Check for positions still marked True
    remaining_true_positions = [pos for pos, value in enumerate(boolean_list) if value]

    # Check if there are no remaining True positions
    if len(remaining_true_positions) == 0:
        print('YES')  # All positions are marked False
    else:
        print('NO')   # There are some positions still marked True

# Example usage (you may uncomment the following lines for testing):
# n = int(input())
# check_if_all_positions_are_false(n)
