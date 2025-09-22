def doMain():
    # Read the first line of input and store it in a variable
    inputString1 = input()
    
    # Read the second line of input and store it in a variable
    inputString2 = input()
    
    # Split the inputs into lists of strings
    numberList1 = inputString1.split()
    numberList2 = inputString2.split()
    
    # Initialize a counter for differences
    differenceCount = 0

    # Compare the first three elements in both lists
    for i in range(3):
        # Convert the string values to integers
        valueA = int(numberList1[i])
        valueB = int(numberList2[i])
        
        # Increment the difference count if values are not equal
        if valueA != valueB:
            differenceCount += 1

    # Output decision based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    doMain()
