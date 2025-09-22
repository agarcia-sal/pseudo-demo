# Define a function to process the boolean values
def process_boolean_values():
    # Step 1: Get the number of boolean values to process
    number_of_values = int(input())
    
    # Step 2: Create a list of boolean values, all initially set to True
    boolean_list = [True] * number_of_values
    
    # Step 3: Initialize variables for iteration
    index_increment = 1
    current_index = 0
    
    # Step 4: Iterate while index_increment is less than or equal to 500000
    while index_increment <= 500000:
        # Step 5: Check if the boolean value at current_index is still True
        if boolean_list[current_index]:
            # Step 6: Set the current value to False
            boolean_list[current_index] = False
        
        # Update index_increment for the next iteration
        index_increment += 1
        
        # Step 7: Calculate the next index by wrapping around the list length
        current_index = (current_index + index_increment) % number_of_values
    
    # Step 8: Filter the list to find any remaining True values
    remaining_true_values = [value for value in boolean_list if value]
    
    # Step 9: Check if there are any values remaining that are still True
    if len(remaining_true_values) == 0:
        # Step 10: If no True values found, print "YES"
        print("YES")
    else:
        # Step 11: If any True values found, print "NO"
        print("NO")

# Uncomment the line below to run the function
# process_boolean_values()
