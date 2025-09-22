def doMain():
    # Input Handling
    input_first_line = input()  # Read the first line of input
    input_second_line = input()  # Read the second line of input
    
    # Split the input lines into lists
    first_list = input_first_line.split()  # Split the first line into parts
    second_list = input_second_line.split()  # Split the second line into parts
    
    # Initialize a Counter
    difference_count = 0  # Variable to keep track of differences

    # Comparison Loop
    for index in range(3):  # Only comparing the first three elements
        first_value = int(first_list[index])  # Convert the element to integer from first list
        second_value = int(second_list[index])  # Convert the element to integer from second list
        
        # Check if the values are not equal
        if first_value != second_value:
            difference_count += 1  # Increment the count if they differ

    # Output Decision
    if difference_count < 3:
        print("YES")  # Print "YES" if differences are less than 3
    else:
        print("NO")  # Print "NO" otherwise

# Function Invocation
doMain()  # Call the function to execute the logic
