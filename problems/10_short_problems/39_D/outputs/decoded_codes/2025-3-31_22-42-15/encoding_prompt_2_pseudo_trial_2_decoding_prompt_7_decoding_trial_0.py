def main():
    # Prompt the user for input
    firstInput = input()
    secondInput = input()
    
    # Split the input into separate components
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count differences
    differenceCount = 0
    
    # Compare the components from both input lists
    for index in range(3):  # Assuming both lists have at least 3 elements
        firstValue = int(firstList[index])  # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer
        
        # Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1  # Increment difference count if values differ
    
    # Determine the output based on differences
    if differenceCount < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

# Execute the main function
main()


     1 2 3
     1 2 4
     

     1 2 3
     4 5 6
     

     1 2 3
     1 2 3
     