def doMain():
    # Read input values for two lists of numbers
    t1 = input()
    t2 = input()
    
    # Split input strings into lists of elements
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a counter for differences
    differenceCount = 0 

    # Iterate over the first three elements of both lists
    for i in range(3):
        # Convert string elements to integers
        a = int(tt1[i])
        b = int(tt2[i])

        # If the elements are different, increment the difference counter
        if a != b:
            differenceCount += 1

    # Check the number of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
doMain()
