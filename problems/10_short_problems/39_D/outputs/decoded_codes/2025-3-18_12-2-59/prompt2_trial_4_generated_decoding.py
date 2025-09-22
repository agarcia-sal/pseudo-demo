# Start the Program

def main():
    # Prompt the user to enter the first line of input and store it
    firstInput = input()
    
    # Prompt the user to enter the second line of input and store it
    secondInput = input()
    
    # Split firstInput into a list of strings
    firstValues = firstInput.split()
    
    # Split secondInput into a list of strings
    secondValues = secondInput.split()
    
    # Initialize differenceCount to keep track of differences
    differenceCount = 0
    
    # Loop through the first three elements of the lists
    for index in range(3):
        # Convert the corresponding elements to integers
        valueFromFirst = int(firstValues[index])
        valueFromSecond = int(secondValues[index])
        
        # Check for inequality and increment differenceCount if they are different
        if valueFromFirst != valueFromSecond:
            differenceCount += 1
            
    # Check the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute Main Function if the Program is the Entry Point
if __name__ == "__main__":
    main()

# End the Program
