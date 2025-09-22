# Function to determine if there are any True values left in the boolean list after updates
def check_boolean_list():
    # Step 1: Accept the size of the boolean list from user input
    n = int(input())

    # Step 2: Create a boolean list of size n with all values initially set to True
    boolean_list = [True] * n

    # Step 3: Initialize index variables
    current_index = 0
    increment = 1

    # Step 4: Loop to update the boolean list
    while increment <= 500000:
        # Step 4a: If the value at the current index is True
        if boolean_list[current_index] is True:
            # Step 4b: Set the value at the current index to False
            boolean_list[current_index] = False
        
        # Step 4c: Update the increment and move to the next index
        increment += 1
        current_index = (current_index + increment) % n  # Wrap around if exceeds n

    # Step 5: Check for any True values left in the boolean list
    remaining_true_values = [value for value in boolean_list if value]

    # Step 6: Determine the result based on the presence of True values
    if len(remaining_true_values) == 0:
        print("YES")  # No True values remain
    else:
        print("NO")   # There are still True values present

# To run the function, uncomment the line below:
# check_boolean_list()
