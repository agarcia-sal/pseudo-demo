def doMain():
    # Input Handling
    inputString1 = input()
    inputString2 = input()
    
    # Split the input strings into lists
    numberList1 = inputString1.split()
    numberList2 = inputString2.split()
    
    # Initialize a counter for differences
    differenceCount = 0

    # Comparison Logic
    for i in range(3):  # Loop through indices 0 to 2
        valueA = int(numberList1[i])  # Convert to integer
        valueB = int(numberList2[i])  # Convert to integer
        
        # Increment the counter if values are different
        if valueA != valueB:
            differenceCount += 1

    # Output Decision
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    doMain()  # Execute the main process
