# Define the main function
def process_boolean_list():
    # Read an integer input
    n = int(input())
    
    # Initialize a boolean list of size n, all set to True
    boolean_list = [True] * n
    
    # Variables to keep track of indices
    j = 0
    i = 1

    # Loop until i exceeds 500000
    while i <= 500000:
        # If the current position is True
        if boolean_list[j]:
            # Set current position to False
            boolean_list[j] = False
        
        # Increment i
        i += 1
        
        # Update j using wrap-around logic
        j = (j + i) % n
    
    # Create a list of True values from boolean_list
    true_values_list = [value for value in boolean_list if value]

    # Check if there are any True values left
    if len(true_values_list) == 0:
        # If no True values, print 'YES'
        print('YES')
    else:
        # If there are True values, print 'NO'
        print('NO')

# You can call the function here to run it
process_boolean_list()
