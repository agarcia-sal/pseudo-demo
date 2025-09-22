def doMain():
    # Read user input for two separate lines
    firstInput = input()
    secondInput = input()
    
    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Using range(3) to iterate over indices 0 to 2
        # Convert the current elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1 
    
    # Check the number of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
doMain()


  Input:
  1 2 3
  1 2 3
  Output: YES
  

  Input:
  1 2 3
  1 2 4
  Output: YES
  

  Input:
  1 2 3
  4 5 6
  Output: NO
  

  Input:
  1 2
  1 3
  Output: YES (only two elements in lists)
  