def main():
    # Prompt the user for the first set of integers
    firstSet = input()
    
    # Prompt the user for the second set of integers
    secondSet = input()
    
    # Split input strings into lists of strings
    firstList = firstSet.split()
    secondList = secondSet.split()
    
    # Initialize difference counter
    differenceCount = 0
    
    # Check each position for differences
    for index in range(3):  # Looping through the first three indices
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # If the values differ, increment the difference counter
        if firstValue != secondValue:
            differenceCount += 1
    
    # Evaluate number of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the main program
if __name__ == "__main__":
    main()


  1 2 3
  1 2 4
  

  5 6 7
  1 2 3
  

  1 2 3
  1 2 3
  