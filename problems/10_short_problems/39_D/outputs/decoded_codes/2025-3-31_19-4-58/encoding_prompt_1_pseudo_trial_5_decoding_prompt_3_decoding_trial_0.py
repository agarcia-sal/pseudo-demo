def main():
    # Read two lines of input representing the sets of values
    firstList = input()
    secondList = input()
    
    # Split the input strings into lists of values
    firstValues = firstList.split()
    secondValues = secondList.split()
    
    # Initialize a counter to track the number of differences
    differenceCount = 0
    
    # Loop through the first three elements (0 to 2 inclusive)
    for x in range(3):
        # Convert the x-th elements to integers
        valueA = int(firstValues[x])
        valueB = int(secondValues[x])
        
        # Increment the difference count if values are not equal
        if valueA != valueB:
            differenceCount += 1
    
    # Check the count of differences and output the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function when the script is executed
if __name__ == "__main__":
    main()


   1 2 3
   1 2 3
   

   4 5 6
   1 2 3
   

   1 2 3
   1 3 3
   