def main():
    # Read input values from the user
    firstInput = input()  # Prompt for the first input string
    secondInput = input()  # Prompt for the second input string
    
    # Split the input strings into lists of components
    firstList = firstInput.split()  # Convert first input string to a list
    secondList = secondInput.split()  # Convert second input string to a list
    
    # Initialize a variable to count differences
    differenceCount = 0
    
    # Compare corresponding elements of both lists
    for index in range(3):  # We will compare only the first 3 elements
        # Convert list elements from strings to integers
        valueFromFirstList = int(firstList[index])  
        valueFromSecondList = int(secondList[index])  
        
        # Check for differences between the two values
        if valueFromFirstList != valueFromSecondList:
            # If they are different, increment the difference count
            differenceCount += 1
    
    # Determine if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")  # There are fewer than 3 differences
    else:
        print("NO")  # There are 3 or more differences

# Execute the main function when the script runs
main()
