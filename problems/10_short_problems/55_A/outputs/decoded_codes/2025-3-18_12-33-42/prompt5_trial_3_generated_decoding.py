# Function to determine if all elements in the list can be marked as False
def check_truth_list():
    # Step 1: Accept user input for the number of elements
    number_of_elements = int(input())
    
    # Step 2: Create a list initialized with 'True' values
    truth_list = [True] * number_of_elements
    
    # Step 3: Initialize counters
    index = 0
    increment = 1

    # Step 4: Loop until increment exceeds 500,000
    while increment <= 500000:
        # Step 5: Check the current index in the truthList 
        if truth_list[index]:
            # Step 6: Mark the current index as 'False'
            truth_list[index] = False
            
        # Step 7: Prepare for the next iteration
        increment += 1
        
        # Step 8: Calculate the next index based on the current index and increment
        index = (index + increment) % number_of_elements
    
    # Step 9: Gather all values from truthList that are still 'True' 
    remaining_true_values = [value for value in truth_list if value]
    
    # Step 10: Check if there are any remaining 'True' values
    if len(remaining_true_values) == 0:
        # Step 11: Output 'YES' if all values were marked 'False'
        print('YES')
    else:
        # Step 12: Output 'NO' if there are still some 'True' values
        print('NO')

# Example of how you might test the function (uncomment to run)
# check_truth_list()
