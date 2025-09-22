def main():
    # Read input values from the user
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of components
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count differences
    differenceCount = 0
    
    # Compare corresponding elements of both lists
    for index in range(3):
        valueFromFirstList = int(firstList[index])
        valueFromSecondList = int(secondList[index])
        
        # Check for differences between the two values
        if valueFromFirstList != valueFromSecondList:
            differenceCount += 1
    
    # Determine if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")  # There are fewer than 3 differences
    else:
        print("NO")   # There are 3 or more differences

# Execute the main function when the script runs
main()
