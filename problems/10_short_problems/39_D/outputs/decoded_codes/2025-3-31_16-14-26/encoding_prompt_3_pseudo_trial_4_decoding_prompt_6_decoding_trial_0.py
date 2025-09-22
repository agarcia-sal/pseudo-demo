def main():
    # Read input values from the user
    first_input = input()  # user input for the first set of values
    second_input = input()  # user input for the second set of values
    
    # Split the input strings into lists of strings
    first_values = first_input.split()  # split the first input into a list
    second_values = second_input.split()  # split the second input into a list
    
    # Initialize a variable to count differences
    difference_count = 0  # start with 0 differences

    # Loop through each value in the lists (assuming they are of the same length of 3)
    for index in range(3):  # loop from 0 to 2
        # Convert string values to integers for comparison
        first_value = int(first_values[index])  # convert first list value to integer
        second_value = int(second_values[index])  # convert second list value to integer

        # Check for differences between corresponding values
        if first_value != second_value:  # if values are not equal
            difference_count += 1  # increment the difference count

    # Decide the output based on the number of differences
    if difference_count < 3:  # if differences are less than 3
        print("YES")  # inputs are similar enough
    else:
        print("NO")  # inputs are too different

# Main execution starts here
main()  # call the main function
