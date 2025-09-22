def process_elements():
    # Step 1: Receive the input value
    number_of_elements = int(input())
    
    # Step 2: Create a boolean list initialized to True
    boolean_list = [True] * number_of_elements
    
    # Step 3: Initialize index and step
    index = 0
    step = 1
    
    # Step 5: Continue as long as step is less than or equal to 500,000
    while step <= 500000:
        # Step 5a: Check if the current index in boolean_list is True
        if boolean_list[index]:
            # Step 5b: Set the current position in boolean_list to False
            boolean_list[index] = False
        
        # Step 5c: Increment step by 1
        step += 1
        
        # Update index with wrap-around using modulo
        index = (index + step) % number_of_elements
    
    # Step 6: Collect all True elements into a new list
    true_elements = [i for i in boolean_list if i]
    
    # Step 7: Check the length of true_elements
    if len(true_elements) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
process_elements()
