def start_main():
    # Read two lines of input
    input1 = input()  # First input
    input2 = input()  # Second input

    # Split the input strings into lists of values
    values1 = input1.split()  # Split the first input string
    values2 = input2.split()  # Split the second input string

    # Initialize a counter for discrepancies
    count_discrepancies = 0  

    # Compare the elements of both lists up to the first three elements
    for index in range(3):  # Loop through indices 0 to 2
        # Convert the current elements to integers
        value_a = int(values1[index])  # Convert the value from the first list
        value_b = int(values2[index])  # Convert the value from the second list
        
        # If the values are not equal, increment the discrepancy counter
        if value_a != value_b:  # Check if values are unequal
            count_discrepancies += 1  # Increment the counter

    # If there are fewer than three discrepancies, print "YES"; otherwise print "NO"
    if count_discrepancies < 3:  # Check the discrepancy count
        print("YES")  # Output for fewer than three discrepancies
    else:
        print("NO")  # Output for three or more discrepancies

# Start the main process
start_main()
