def start_main():
    # Read two lines of input
    input1 = input()
    input2 = input()

    # Split the input strings into lists of values
    values1 = input1.split()
    values2 = input2.split()

    # Initialize a counter for discrepancies
    count_discrepancies = 0

    # Compare the elements of both lists up to the first three elements
    for index in range(3):
        # Convert the current elements to integers
        value_a = int(values1[index])
        value_b = int(values2[index])
        
        # If the values are not equal, increment the discrepancy counter
        if value_a != value_b:
            count_discrepancies += 1

    # If there are fewer than three discrepancies, print "YES"; otherwise print "NO"
    if count_discrepancies < 3:
        print("YES")
    else:
        print("NO")

# Start the main process
start_main()
