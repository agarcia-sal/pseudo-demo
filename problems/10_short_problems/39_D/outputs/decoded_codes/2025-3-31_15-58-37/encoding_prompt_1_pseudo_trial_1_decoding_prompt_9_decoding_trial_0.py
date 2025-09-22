def doMain():
    # Input Handling
    inputString1 = input()  # First line of input
    inputString2 = input()  # Second line of input
    
    # Split the input strings into lists of numbers as strings
    numberList1 = inputString1.split()
    numberList2 = inputString2.split()
    
    # Initialize a Counter for differences
    differenceCount = 0
    
    # Comparison Logic: Check up to the first 3 elements
    for i in range(3):  # Loop through indices 0 to 2
        valueA = int(numberList1[i])  # Convert element to integer from list 1
        valueB = int(numberList2[i])  # Convert element to integer from list 2
        
        # Check if values are not equal
        if valueA != valueB:
            differenceCount += 1  # Increment difference count if they differ
    
    # Output Decision based on the count of differences
    if differenceCount < 3:
        print("YES")  # Output YES if differences are less than 3
    else:
        print("NO")   # Output NO if differences are 3 or more

# Program Execution
if __name__ == "__main__":
    doMain()  # Call the main function to execute the process
