def doMain():
    # Get input from the user
    inputString1 = input()  # Prompt user for the first input string
    inputString2 = input()  # Prompt user for the second input string
    
    # Split each input string into a list of strings
    list1 = inputString1.split()  # List of words from inputString1
    list2 = inputString2.split()  # List of words from inputString2
    
    # Initialize a counter for differences
    differenceCount = 0

    # Compare each corresponding element in the two lists
    for index in range(3):  # Iterating over indices 0, 1, and 2
        valueFromList1 = int(list1[index])  # Convert current element to integer
        valueFromList2 = int(list2[index])  # Convert current element to integer
        
        # Check if the values are different
        if valueFromList1 != valueFromList2:  # Check if the two values are not equal
            # Increment the difference count
            differenceCount += 1
            
    # Evaluate the total number of differences
    if differenceCount < 3:
        print("YES")  # Output if fewer than 3 differences
    else:
        print("NO")  # Output if 3 or more differences

# Main block to execute the function
if __name__ == "__main__":
    doMain()  # Call the main function
