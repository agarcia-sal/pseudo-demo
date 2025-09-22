def doMain():
    # Prompt for user input
    inputString1 = input()
    inputString2 = input()
    
    # Process the input
    listOfValues1 = inputString1.split()
    listOfValues2 = inputString2.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare values at corresponding indices
    for i in range(3):  # Loop through the first three indices (0, 1, 2)
        valueA = int(listOfValues1[i])  # Convert to integer
        valueB = int(listOfValues2[i])  # Convert to integer
        
        # Increment the difference count if values are not equal
        if valueA != valueB:
            differenceCount += 1
    
    # Determine the output based on the difference count
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program
if __name__ == "__main__":
    doMain()


  1 2 3
  1 2 4
  

  1 2 3
  4 5 6
  