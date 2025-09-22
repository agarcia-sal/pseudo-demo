def main():
    # Read input from the user
    firstInput = input()
    secondInput = input()
    
    # Split the first input into separate elements and store them in a list
    firstList = firstInput.split()
    
    # Split the second input into separate elements and store them in a list
    secondList = secondInput.split()
    
    # Initialize a variable to count the differences
    differenceCount = 0
    
    # Iterate over the indices of the lists
    for index in range(3):  # We know there are exactly 3 elements to compare
        firstValue = int(firstList[index])  # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer
        
        # Check if values are different
        if firstValue != secondValue:
            differenceCount += 1  # Increment difference count if values are different
    
    # Output "YES" if fewer than 3 differences exist
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function when the program runs
main()
