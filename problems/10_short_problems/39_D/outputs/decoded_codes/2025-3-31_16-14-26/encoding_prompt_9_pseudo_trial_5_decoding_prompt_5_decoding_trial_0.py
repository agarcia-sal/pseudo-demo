def doMain():
    # Receive first input and store it as a string
    first_input = input()
    # Receive second input and store it as a string
    second_input = input()
    
    # Split inputs into lists of strings
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the range for three comparisons
    for i in range(3):
        # Convert the elements to integers for comparison
        value_from_first = int(first_list[i])
        value_from_second = int(second_list[i])
        
        # If the two values are not equal, increment the difference count
        if value_from_first != value_from_second:
            difference_count += 1
    
    # Check the number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the function when the program starts
doMain()
