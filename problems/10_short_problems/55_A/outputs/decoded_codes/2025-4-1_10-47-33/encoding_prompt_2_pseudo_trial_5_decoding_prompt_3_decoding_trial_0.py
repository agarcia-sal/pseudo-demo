def main():
    # Step 1: Get the total number of elements from user input
    total_elements = int(input())
    
    # Step 2: Initialize the boolean list with all elements set to True
    boolean_list = [True] * total_elements
    
    # Step 3: Initialize current index and increment
    current_index = 0
    increment = 1
    
    # Step 4: Begin the loop for increments up to 500,000
    while increment <= 500000:
        # Step 5: Check the status at current index
        if boolean_list[current_index]:
            # Step 6: Set the current index to False
            boolean_list[current_index] = False
            
        # Step 7: Increment and update current index
        increment += 1
        current_index = (current_index + increment) % total_elements
    
    # Step 8: Collect the remaining True values
    remaining_true_values = [value for value in boolean_list if value]
    
    # Step 9: Determine and output the result based on the length of remaining true values
    if len(remaining_true_values) == 0:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
