def main_procedure():
    # Read the first list of integers as a string
    first_input = input()  # User input for the first list
    
    # Read the second list of integers as a string
    second_input = input()  # User input for the second list
    
    # Split the input strings into lists of integers
    first_list = [int(x) for x in first_input.split()]  # Convert to list of integers
    second_list = [int(x) for x in second_input.split()]  # Convert to list of integers
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Compare the integers in the two lists
    for index in range(3):  # Loop over the range of 3
        first_value = first_list[index]  # Current value from the first list
        second_value = second_list[index]  # Current value from the second list
        
        # If the values differ, increase the difference count
        if first_value != second_value:
            difference_count += 1  # Incrementing the difference count
    
    # Check the count of differences to determine the output
    if difference_count < 3:
        print("YES")  # If differences are less than 3
    else:
        print("NO")  # If differences are 3 or more

# Execute the main procedure
main_procedure()
