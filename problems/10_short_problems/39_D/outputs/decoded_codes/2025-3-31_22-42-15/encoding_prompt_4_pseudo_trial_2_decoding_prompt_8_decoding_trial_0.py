def doMain():
    # Read input values
    firstLine = input()
    secondLine = input()
    
    # Split input lines into lists of strings
    list1 = firstLine.split()
    list2 = secondLine.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        valueA = int(list1[index])
        valueB = int(list2[index])
        
        # Check if values are different
        if valueA != valueB:
            # Increment the difference counter
            differenceCount += 1
    
    # Check the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
doMain()
