def start_main():
    # Read two lines of input
    input1 = input()  # First line of input
    input2 = input()  # Second line of input

    # Split the input strings into lists of values
    values1 = input1.split()  # Split the first input into a list
    values2 = input2.split()  # Split the second input into a list

    # Initialize a counter for discrepancies
    count_discrepancies = 0 

    # Compare the elements of both lists up to the first three elements
    for index in range(3):  # Loop through the first three indices (0, 1, 2)
        # Convert the current elements to integers
        value_a = int(values1[index])  # Convert the element from the first list to integer
        value_b = int(values2[index])  # Convert the element from the second list to integer
        
        # If the values are not equal, increment the discrepancy counter
        if value_a != value_b:  # Check if the two values are different
            count_discrepancies += 1  # Increment the discrepancy count

    # If there are fewer than three discrepancies, print "YES"; otherwise print "NO"
    if count_discrepancies < 3:
        print("YES")  # Print YES if discrepancies are less than 3
    else:
        print("NO")  # Print NO if discrepancies are 3 or more

# Start the main process
start_main()
