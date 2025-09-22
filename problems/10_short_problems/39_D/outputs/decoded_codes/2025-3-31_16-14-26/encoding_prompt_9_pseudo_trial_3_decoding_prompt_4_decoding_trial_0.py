def doMain():
    # Read two lines of input containing numeric values
    first_sequence = input().split()
    second_sequence = input().split()
    
    difference_count = 0

    # Compare corresponding values in the two sequences
    for index in range(3):
        first_value = int(first_sequence[index])
        second_value = int(second_sequence[index])
        
        # Increment the difference count if values are not equal
        if first_value != second_value:
            difference_count += 1

    # Determine output based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program starts
doMain()


     1 2 3
     1 2 3
     

     1 2 3
     1 4 3
     

     1 2 3
     4 5 3
     

     1 2 3
     4 5 6
     