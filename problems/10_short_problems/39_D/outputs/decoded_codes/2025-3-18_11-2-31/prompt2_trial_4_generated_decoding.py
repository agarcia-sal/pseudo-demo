def doMain():
    # Get two inputs from the user representing two sets of values
    firstSet = input()
    secondSet = input()
    
    # Split the input values into lists
    firstValues = firstSet.split()
    secondValues = secondSet.split()
    
    # Initialize a counter to track differing values
    differenceCount = 0 

    # Loop through each of the first three values in both lists
    for index in range(3):        
        # Convert the current values at the index from the string list to integers
        valueFromFirstSet = int(firstValues[index])
        valueFromSecondSet = int(secondValues[index])
        
        # Check if the values from both sets are different
        if valueFromFirstSet != valueFromSecondSet:            
            # Increment the counter when a difference is found
            differenceCount += 1 

    # Determine the output based on the number of differences found
    if differenceCount < 3:
        print("YES")  # Indicating fewer than 3 differences
    else:
        print("NO")   # Indicating 3 or more differences

# The main function executes when the program starts
if __name__ == "__main__":
    doMain()  # Initiates the logic defined above
