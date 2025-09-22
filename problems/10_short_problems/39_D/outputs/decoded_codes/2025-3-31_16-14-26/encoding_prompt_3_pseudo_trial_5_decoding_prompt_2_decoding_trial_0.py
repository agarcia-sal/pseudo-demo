def doMain():
    # Get input from the user
    inputString1 = input()  # First input string
    inputString2 = input()  # Second input string
    
    # Split each input string into a list of strings
    list1 = inputString1.split()  # List of words from inputString1
    list2 = inputString2.split()  # List of words from inputString2
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare each corresponding element in the two lists
    for index in range(3):  # Assuming there are at least 3 elements to compare
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
