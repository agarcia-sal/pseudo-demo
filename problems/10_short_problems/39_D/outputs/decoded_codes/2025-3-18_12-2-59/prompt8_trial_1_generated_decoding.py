def main():
    # Read input values from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of values
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0 

    # Loop through the first three values of each list
    for index in range(3):
        # Convert string values to integers for comparison
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1 

    # Check the number of differences
    if differenceCount < 3 and differenceCount > 0:
        print("YES")
    else:
        print("NO")

# Main execution starts here
main()


   1 2 3
   1 2 3
   

   1 2 3
   4 2 3
   

   1 2 3
   4 5 6
   

   1 2 3
   4 2 5
   

   1 1 1
   2 2 2
   