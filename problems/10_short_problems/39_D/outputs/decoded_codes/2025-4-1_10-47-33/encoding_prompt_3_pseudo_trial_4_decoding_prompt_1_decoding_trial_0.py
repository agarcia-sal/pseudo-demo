def main():
    # Read input from the user
    firstInput = input()  # firstInput as STRING
    secondInput = input()  # secondInput as STRING

    # Split input strings into lists
    firstList = firstInput.split()  # firstList as LIST OF STRINGS
    secondList = secondInput.split()  # secondList as LIST OF STRINGS

    # Initialize a counter for differences
    differenceCount = 0  # differenceCount as INTEGER

    # Check the first three elements of both lists
    for index in range(3):  # FOR EACH index FROM 0 TO 2
        # Convert the current elements to integers
        firstValue = int(firstList[index])  # firstValue as INTEGER
        secondValue = int(secondList[index])  # secondValue as INTEGER

        # Compare elements and count differences
        if firstValue != secondValue:  # IF firstValue IS NOT EQUAL TO secondValue
            differenceCount += 1  # INCREMENT differenceCount BY 1

    # Determine result based on the number of differences
    if differenceCount < 3:  # IF differenceCount IS LESS THAN 3
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":  # IF this file IS the main module
    main()  # CALL main
