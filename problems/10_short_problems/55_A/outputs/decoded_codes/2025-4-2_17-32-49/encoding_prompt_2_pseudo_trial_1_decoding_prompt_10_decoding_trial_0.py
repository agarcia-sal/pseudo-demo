def process_boolean_list():
    # Step 1: Receive input value for the number of elements
    number_of_elements = int(input())

    # Step 2: Create a list initialized to True
    boolean_list = [True] * number_of_elements

    # Step 3: Set the initial index and step
    index = 0
    step = 1

    # Step 5: Process the list as long as step is less than or equal to 500,000
    while step <= 500000:
        # Check if the current position in booleanList is True
        if boolean_list[index]:
            # Change the current position to False
            boolean_list[index] = False
        
        # Increment the step variable
        step += 1
        # Update the index with wrapping around logic
        index = (index + step) % number_of_elements

    # Step 6: Collect all True elements into a new list
    true_elements = [i for i, val in enumerate(boolean_list) if val]

    # Step 7: Check the length of trueElements and print the appropriate message
    if len(true_elements) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute the code
process_boolean_list()
