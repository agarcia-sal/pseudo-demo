def main():
    # Read two lines of input
    firstInput = input()
    secondInput = input()
    
    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count differences
    differenceCount = 0 
    
    # Loop through the first three positions of both lists
    for index in range(3):
        # Convert the current elements of each list to integers
        numberFromFirstList = int(firstList[index])
        numberFromSecondList = int(secondList[index])
        
        # Check if the numbers at the current position are different
        if numberFromFirstList != numberFromSecondList:
            # Increment the difference counter
            differenceCount += 1
    
    # Determine if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
