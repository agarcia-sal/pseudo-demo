def do_main():
    # Prompt the user for the first time input and store it
    t1 = input()
    
    # Prompt the user for the second time input and store it
    t2 = input()
    
    # Split the inputs into lists of time components
    time_components1 = t1.split(':')
    time_components2 = t2.split(':')
    
    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three elements of each input
    for index in range(3):
        # Convert the corresponding time components to integers
        component_a = int(time_components1[index])
        component_b = int(time_components2[index])
        
        # If the components from the two times are not equal
        if component_a != component_b:
            # Increment the difference counter
            difference_count += 1 

    # Check the number of differences
    if difference_count < 3:
        # Output "YES" if differences are fewer than 3
        print("YES")
    else:
        # Output "NO" if differences are 3 or more
        print("NO")

# Main program execution
do_main()
