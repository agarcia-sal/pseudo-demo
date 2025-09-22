def main():
    # Get input from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of numbers
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize the difference counter
    differenceCount = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the corresponding elements to integers for comparison
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        # If the numbers are not equal, increase the difference counter
        if firstNumber != secondNumber:
            differenceCount += 1
            
    # Check the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()


     1 2 3
     1 2 4
     

     4 5 6
     4 5 6
     

     7 8 9
     10 11 12
     

     1 1 1
     1 1 1
     

     1 2 3
     3 2 1
     