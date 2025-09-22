def doMain():
    # Read two strings from user input
    string1 = input()
    string2 = input()
    
    # Split input strings into lists of substrings
    list1 = string1.split()
    list2 = string2.split()
    
    # Initialize a counter for differences
    differenceCount = 0 
    
    # Compare the first three elements of both lists
    for index in range(3):
        # Convert list elements to integers for comparison
        valueFromList1 = int(list1[index])
        valueFromList2 = int(list2[index])
        
        # Check if the values are different
        if valueFromList1 != valueFromList2:
            differenceCount += 1
            
    # Determine if less than three differences were found
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program execution
if __name__ == "__main__":
    doMain()
