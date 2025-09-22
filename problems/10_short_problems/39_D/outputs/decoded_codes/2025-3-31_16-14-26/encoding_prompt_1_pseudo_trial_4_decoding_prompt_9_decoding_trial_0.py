def start_main():
    # Read two lines of input
    input1 = input()  # First input line
    input2 = input()  # Second input line
    
    # Split the input strings into lists of values
    values1 = input1.split()  # Convert the first input into a list of strings
    values2 = input2.split()  # Convert the second input into a list of strings
    
    # Initialize a counter for discrepancies
    count_discrepancies = 0 

    # Compare the elements of both lists up to the first three elements
    for index in range(3):  # Loop through the first three indices
        # Convert the current elements to integers
        value_a = int(values1[index])  # Convert value from first list to integer
        value_b = int(values2[index])  # Convert value from second list to integer
        
        # If the values are not equal, increment the discrepancy counter
        if value_a != value_b:
            count_discrepancies += 1  # Increment discrepancy count
    
    # If there are fewer than three discrepancies, print "YES"; otherwise print "NO"
    if count_discrepancies < 3:
        print("YES")
    else:
        print("NO")

# Start the main process
start_main()
