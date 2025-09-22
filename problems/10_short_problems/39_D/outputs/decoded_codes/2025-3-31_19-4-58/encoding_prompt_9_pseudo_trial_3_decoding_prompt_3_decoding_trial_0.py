# Start the main program
def main():
    # Prompt the user for the first set of integers
    firstSet = input()
    # Prompt the user for the second set of integers
    secondSet = input()
    
    # Split input strings into lists
    firstList = firstSet.split()
    secondList = secondSet.split()
    
    # Initialize difference counter
    differenceCount = 0
    
    # Check each position for differences
    for index in range(3):  # Loop through indices 0, 1, and 2
        firstValue = int(firstList[index])   # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer
        
        # Increment difference count if values are not equal
        if firstValue != secondValue:
            differenceCount += 1

    # Evaluate number of differences
    if differenceCount < 3:
        print("YES")  # Output if differences are less than 3
    else:
        print("NO")   # Output if differences are 3 or more

# Call the main function to execute the program
main()
