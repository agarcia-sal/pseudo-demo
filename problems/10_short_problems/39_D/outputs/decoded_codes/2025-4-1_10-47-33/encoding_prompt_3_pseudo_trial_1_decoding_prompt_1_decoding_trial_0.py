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
    for index in range(3):  # Loop from 0 to 2 (inclusive)
        valueFromFirstTest = int(firstTestList[index])  # Convert to INTEGER
        valueFromSecondTest = int(secondTestList[index])  # Convert to INTEGER
        
        # Check if the values from both test cases are different
        if valueFromFirstTest != valueFromSecondTest:  # Not equal
            differenceCount += 1  # Increment counter

    # Decide if the number of differences is acceptable
    if differenceCount < 3:  # Less than 3 differences
        print("YES")
    else:
        print("NO")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    doMain()
