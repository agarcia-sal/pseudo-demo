# Function to process the pseudocode logic
def process_input():
    # Input: Read an integer value 'n' from user
    n = int(input())
    
    # Initialize a boolean list 'b' of size 'n' with all values set to True
    boolean_list = [True] * n
    
    # Initialize variables 
    index = 0  # This will act as an index for the list 'b'
    counter = 1  # This is a counter that will increment in the loop

    # Loop to perform operations while 'counter' is less than or equal to 500000
    while counter <= 500000:
        # Check if the current index 'index' in the list 'boolean_list' is True
        if boolean_list[index]:
            # Set the current index 'index' to False
            boolean_list[index] = False
        
        # Increment 'counter' by 1
        counter += 1
        
        # Update index by adding the current value of 'counter', and taking modulo n
        index = (index + counter) % n

    # Filter the list 'b' to collect all elements that are still True
    filtered_list = [value for value in boolean_list if value]

    # Check if the filtered list 'filtered_list' is empty
    if len(filtered_list) == 0:
        # Output 'YES' if list 'filtered_list' is empty
        print('YES')
    else:
        # Output 'NO' if list 'filtered_list' is not empty
        print('NO')

# Call the function to execute the logic
process_input()
