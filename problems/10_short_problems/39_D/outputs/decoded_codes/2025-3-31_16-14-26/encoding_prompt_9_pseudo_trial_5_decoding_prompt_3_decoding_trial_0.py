def doMain():
    # Receive inputs
    firstInput = input()
    secondInput = input()

    # Split inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Loop through the range from 0 to 2 for three comparisons
    for i in range(3):
        # Convert elements to integers
        valueFromFirst = int(firstList[i])
        valueFromSecond = int(secondList[i])

        # Increment counter if values are not equal
        if valueFromFirst != valueFromSecond:
            differenceCount += 1

    # Check the number of differences and output result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the function when the program starts
doMain()


   1 2 3
   1 2 2
   

   YES
   

   5 6 7
   5 6 9
   

   YES
   

   8 9 10
   8 7 6
   

   NO
   

   0 0 0
   1 2 3
   

   YES
   

   5 10 15
   5 10 15
   

   YES
   