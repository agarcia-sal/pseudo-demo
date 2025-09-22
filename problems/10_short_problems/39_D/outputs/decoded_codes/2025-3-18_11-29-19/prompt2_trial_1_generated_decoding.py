# Start the Program

def main():
    # Prompt the user to enter the first string of numbers
    firstInput = input()
    
    # Prompt the user to enter the second string of numbers
    secondInput = input()
    
    # Split firstInput into individual elements and store them in firstList
    firstList = firstInput.split()
    
    # Split secondInput into individual elements and store them in secondList
    secondList = secondInput.split()
    
    # Initialize a variable differenceCount to 0
    differenceCount = 0
    
    # Iterate over the first three elements of both lists
    for index in range(3):  # Iterate from 0 to 2
        # Convert the value at the current index in firstList into an integer
        firstValue = int(firstList[index])
        
        # Convert the value at the current index in secondList into an integer
        secondValue = int(secondList[index])
        
        # If firstValue is not equal to secondValue
        if firstValue != secondValue:
            # Increment differenceCount by 1
            differenceCount += 1

    # Evaluate the count of differences
    if differenceCount < 3:
        # Display the message "YES"
        print("YES")
    else:
        # Display the message "NO"
        print("NO")

# Execute the main function when the program starts
if __name__ == "__main__":
    main()

# End the Program
