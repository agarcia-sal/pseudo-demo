def main():
    # Prompt the user for two sets of numbers
    firstInput = input()
    secondInput = input()
    
    # Split the inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare corresponding elements from both lists
    for index in range(3):  # Iterate from 0 to 2
        # Convert the current elements to integers for comparison
        numberFromFirstList = int(firstList[index])
        numberFromSecondList = int(secondList[index])
        
        # Check if the numbers are different
        if numberFromFirstList != numberFromSecondList:
            differenceCount += 1  # Increment difference count
    
    # Evaluate the number of differences 
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# This part indicates that the main function will run when the script is executed
if __name__ == "__main__":
    main()
