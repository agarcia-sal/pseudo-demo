def doMain():
    # Input Handling: Read input strings
    inputString1 = input()
    inputString2 = input()
    
    # Split input strings into lists of numbers
    numberList1 = inputString1.split()
    numberList2 = inputString2.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Comparison Logic: Compare corresponding elements
    for i in range(3):  # Only compare the first three elements
        valueA = int(numberList1[i])  # Convert to integer
        valueB = int(numberList2[i])  # Convert to integer
        if valueA != valueB:  # Check if they are not equal
            differenceCount += 1  # Increment the difference count

    # Output Decision based on the count of differences
    if differenceCount < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

# Program Execution: Run the main function if the script is executed
if __name__ == "__main__":
    doMain()
