def doMain():
    # Read input values for two lists of numbers
    t1 = input()  # Read the first line of input
    t2 = input()  # Read the second line of input
    
    # Split input strings into lists of elements
    tt1 = t1.split()  # Split the first input string into a list
    tt2 = t2.split()  # Split the second input string into a list
    
    # Initialize a counter for differences
    differenceCount = 0  # Counter to track the number of differences

    # Iterate over the first three elements of both lists
    for i in range(3):  # Loop through indices 0 to 2 (inclusive)
        # Convert string elements to integers
        a = int(tt1[i])  # Convert the i-th element of tt1 to an integer
        b = int(tt2[i])  # Convert the i-th element of tt2 to an integer

        # If the elements are different, increment the difference counter
        if a != b:  # Check if the two integers are not equal
            differenceCount += 1  # Increment the counter if they are different

    # Check the number of differences and print the result
    if differenceCount < 3:  # If the number of differences is less than 3
        print("YES")  # Print YES if the condition is met
    else:
        print("NO")  # Print NO otherwise

# Main execution starts here
doMain()  # Call the function to execute the program
