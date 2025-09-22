def doMain():
    # Input Handling
    inputString1 = input()
    inputString2 = input()
    
    # Splitting input strings into lists
    numberList1 = inputString1.split()
    numberList2 = inputString2.split()
    
    # Initialize a Counter
    differenceCount = 0
    
    # Comparison Logic
    for i in range(3):
        valueA = int(numberList1[i])
        valueB = int(numberList2[i])
        
        if valueA != valueB:
            differenceCount += 1
    
    # Output Decision
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Program Execution
if __name__ == "__main__":
    doMain()
