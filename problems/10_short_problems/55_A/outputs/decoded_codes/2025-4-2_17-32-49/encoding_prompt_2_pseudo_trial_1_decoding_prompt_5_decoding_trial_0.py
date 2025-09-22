# Function to process the boolean list based on the input number of elements
def boolean_list_process():
    # Step 1: Receive input for the number of elements
    number_of_elements = int(input())
    
    # Step 2: Create a list initialized to True
    boolean_list = [True] * number_of_elements
    
    # Step 3: Initialize variables for the current position and step increment
    index = 0
    step = 1
    
    # Step 5: Process while step is less than or equal to 500,000
    while step <= 500000:
        # Step 5a: Check if the current position is True
        if boolean_list[index]:
            # Step 5b: Change the current position to False
            boolean_list[index] = False
        
        # Step 5c: Increment step and update index
        step += 1
        index = (index + step) % number_of_elements
    
    # Step 6: Collect True elements into a new list
    true_elements = [i for i in boolean_list if i]
    
    # Step 7: Check the length of true_elements
    if len(true_elements) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
boolean_list_process()
