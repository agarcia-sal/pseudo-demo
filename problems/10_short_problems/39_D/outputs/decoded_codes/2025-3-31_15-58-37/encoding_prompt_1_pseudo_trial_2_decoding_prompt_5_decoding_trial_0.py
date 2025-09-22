def doMain():
    # Get two lines of input from the user
    first_input = input()
    second_input = input()
    
    # Split the inputs into separate components
    split_first_input = first_input.split()
    split_second_input = second_input.split()
    
    # Initialize a variable to count the number of differences
    difference_count = 0 

    # Iterate through the first three elements of both inputs
    for index in range(3):
        # Convert the current elements to integers
        first_value = int(split_first_input[index])
        second_value = int(split_second_input[index])
        
        # Check if the two values are different
        if first_value != second_value:
            # Increment the count of differences
            difference_count += 1 
    
    # If the number of differences is less than 3, print "YES", otherwise print "NO"
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution flow
doMain()
