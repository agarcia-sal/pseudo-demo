def main():
    # Prompt user for two inputs
    first_input = input()  # Get first input from the user
    second_input = input()  # Get second input from the user
    
    # Split the inputs into lists of values
    first_list = first_input.split()  # Split the first input string into a list of values
    second_list = second_input.split()  # Split the second input string into a list of values
    
    # Initialize a counter for differences
    difference_count = 0  # Initialize the counter for differing values
    
    # Iterate over the first three elements of both lists
    for index in range(3):  # Loop over the indices 0 to 2
        first_value = int(first_list[index])  # Convert the current value from the first list to an integer
        second_value = int(second_list[index])  # Convert the current value from the second list to an integer
        
        # Check if the current values are different
        if first_value != second_value:  # If the values are not equal
            difference_count += 1  # Increment the count of differences

    # Decide the output based on the number of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Print yes if differences are less than 3
    else:  # Otherwise
        print("NO")  # Print no if differences are 3 or more

# Start program execution
main()
