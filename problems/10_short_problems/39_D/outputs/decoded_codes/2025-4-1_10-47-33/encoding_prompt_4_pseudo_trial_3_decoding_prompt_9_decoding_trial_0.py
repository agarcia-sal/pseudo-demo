def doMain():
    # Read two lines of input
    firstLine = input()
    secondLine = input()
    
    # Split the input lines into lists of strings
    list1 = firstLine.split()
    list2 = secondLine.split()
    
    # Initialize a counter for different values
    differenceCount = 0
    
    # Compare the first three elements in both lists
    for index in range(3):  # Loop through indices 0 to 2
        # Convert the current elements to integers
        valueA = int(list1[index])
        valueB = int(list2[index])
        
        # If the values are not equal, increment the difference counter
        if valueA != valueB:
            differenceCount += 1
            
    # Check if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main program execution starts here
doMain()
