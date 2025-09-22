def doMain():
    # Get input from the user
    inputString1 = input()  # First input string
    inputString2 = input()  # Second input string
    
    # Split each input string into a list of words
    list1 = inputString1.split()  # List of words from the first input
    list2 = inputString2.split()  # List of words from the second input
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare each corresponding element in the two lists
    for index in range(3):  # We are assuming the lists are at least of length 3
        # Convert the current elements to integers
        valueFromList1 = int(list1[index])
        valueFromList2 = int(list2[index])
        
        # Check if the values are different
        if valueFromList1 != valueFromList2:
            # Increment the difference count
            differenceCount += 1
            
    # Evaluate the total number of differences
    if differenceCount < 3:
        print("YES")  # Output if differences are less than 3
    else:
        print("NO")   # Output if differences are 3 or more

# Main block to execute the function
if __name__ == "__main__":
    doMain()
