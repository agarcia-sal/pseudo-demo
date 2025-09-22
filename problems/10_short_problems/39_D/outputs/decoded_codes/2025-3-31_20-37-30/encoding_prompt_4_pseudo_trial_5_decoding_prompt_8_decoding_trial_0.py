def doMain():
    # Read input values
    input1 = input()
    input2 = input()
    
    # Split input strings into lists
    list1 = input1.split()
    list2 = input2.split()
    
    # Ensure both lists have at least 3 elements for comparison
    if len(list1) < 3 or len(list2) < 3:
        print("NO")
        return

    # Initialize the result counter
    mismatchCount = 0

    # Compare corresponding elements in both lists
    for index in range(3):
        value1 = int(list1[index])
        value2 = int(list2[index])
        
        if value1 != value2:
            mismatchCount += 1
        
    # Determine if the number of mismatches is less than 3
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Main entry point
doMain()
