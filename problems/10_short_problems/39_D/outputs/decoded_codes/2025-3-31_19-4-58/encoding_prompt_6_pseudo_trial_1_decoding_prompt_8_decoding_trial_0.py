def MainProcedure():
    # Read the first line of input and store it as string1
    string1 = input()
    
    # Read the second line of input and store it as string2
    string2 = input()
    
    # Split each input string into a list of strings
    list1 = string1.split()
    list2 = string2.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Loop through the first three elements of each list
    for index in range(3):
        # Convert the current elements to integers
        numberFromList1 = int(list1[index])
        numberFromList2 = int(list2[index])
        
        # Check if the two numbers are different
        if numberFromList1 != numberFromList2:
            # Increment the difference counter
            differenceCount += 1
    
    # If the count of differences is less than 3, print "YES"
    if differenceCount < 3:
        print("YES")
    else:
        # If the count of differences is 3 or more, print "NO"
        print("NO")

# Start the program by calling the MainProcedure
MainProcedure()
