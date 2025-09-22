# Function to determine the existence of TRUE values after a simulation process
def simulate_boolean_list():
    # Step 1: Input integer value n
    n = int(input())

    # Step 2: Initialize a list of boolean values
    boolean_list = [True] * n
    
    # Step 3: Initialize variables
    j = 0  # Index in the boolean list
    i = 1  # Incrementer for the loop

    # Step 4: Loop until i exceeds 500000
    while i <= 500000:
        # Step 5: Check if the current index in the boolean list is TRUE
        if boolean_list[j]:
            # Step 6: Set the current index to FALSE
            boolean_list[j] = False
            
        # Step 7: Increment i
        i += 1
        
        # Step 8: Update j to the next index in a circular manner
        j = (j + i) % n

    # Step 9: Create a list of all TRUE values in boolean_list
    true_values_list = [value for value in boolean_list if value]

    # Step 10: Check if there are no TRUE values in true_values_list
    if len(true_values_list) == 0:
        # Step 11: Print 'YES' if no TRUE values exist
        print('YES')
    else:
        # Step 12: Print 'NO' if TRUE values exist
        print('NO')

# Run the function
simulate_boolean_list()
