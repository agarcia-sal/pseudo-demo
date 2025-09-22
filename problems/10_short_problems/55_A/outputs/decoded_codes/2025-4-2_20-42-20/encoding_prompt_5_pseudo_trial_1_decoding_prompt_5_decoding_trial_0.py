# Function to determine if all positions in the marks list end up being False
def check_positions():
    # Step 1: Get the size of the list from user input
    number_of_positions = int(input())
    
    # Step 2: Initialize marks list tracking the status of each position
    marks = [True] * number_of_positions
    
    # Step 3: Initialize counters
    current_index = 0  # Tracking our current position in the list
    increment_value = 1  # Step size for marking
    
    # Step 4: Loop until increment_value exceeds 500,000
    while increment_value <= 500000:
        # Step 5: Check if the current position is still marked as True
        if marks[current_index]:
            # Step 6: Mark the current position as False
            marks[current_index] = False
            
        # Step 7: Prepare for the next iteration
        increment_value += 1  # Increase the step size
        current_index = (current_index + increment_value) % number_of_positions  # Update current index

    # Step 8: Filter the marks list to find any still marked as True
    remaining_true_positions = [mark for mark in marks if mark]  # New list of True marks

    # Step 9: Check the result of the filtering
    if len(remaining_true_positions) == 0:
        # If there are no True positions left, print "YES"
        print('YES')
    else:
        # If there are still True positions left, print "NO"
        print('NO')

# Example execution (you can uncomment the line below to run the function in a proper environment)
# check_positions()
