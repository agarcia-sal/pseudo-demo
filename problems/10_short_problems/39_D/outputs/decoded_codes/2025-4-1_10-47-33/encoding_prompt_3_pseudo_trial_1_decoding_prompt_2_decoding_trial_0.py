def doMain():
    # Read input values for two test cases
    firstTestCase = input()
    secondTestCase = input()
    
    # Split the input strings into lists of strings
    firstTestList = firstTestCase.split()
    secondTestList = secondTestCase.split()

    # Initialize count of differences
    differenceCount = 0

    # Compare corresponding elements of both test cases
    for index in range(3):  # Loop through indices 0 to 2
        valueFromFirstTest = int(firstTestList[index])  # Convert to integer
        valueFromSecondTest = int(secondTestList[index])  # Convert to integer
        
        # Check if the values from both test cases are different
        if valueFromFirstTest != valueFromSecondTest:
            differenceCount += 1  # Increment difference count

    # Decide if the number of differences is acceptable
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    doMain()
