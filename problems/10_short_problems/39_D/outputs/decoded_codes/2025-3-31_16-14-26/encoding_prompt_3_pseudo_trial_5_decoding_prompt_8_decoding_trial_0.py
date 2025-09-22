def doMain():
    # Get input from the user
    inputString1 = input()
    inputString2 = input()
    
    # Split each input string into a list of strings
    list1 = inputString1.split()
    list2 = inputString2.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare each corresponding element in the two lists
    for index in range(3):
        # Convert the current elements to integers
        valueFromList1 = int(list1[index])
        valueFromList2 = int(list2[index])
        
        # Check if the values are different
        if valueFromList1 != valueFromList2:
            # Increment the difference count
            differenceCount += 1
            
    # Evaluate the total number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main block to execute the function
if __name__ == "__main__":
    doMain()
