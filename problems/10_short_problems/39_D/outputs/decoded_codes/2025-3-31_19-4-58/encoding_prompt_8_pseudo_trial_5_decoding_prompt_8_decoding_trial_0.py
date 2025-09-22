def main():
    # Read two lines of input representing two sets of numbers
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of numbers
    firstNumbers = firstInput.split()
    secondNumbers = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Iterate through the numbers at each corresponding position
    for index in range(3):
        # Convert the string numbers to integers
        firstNumber = int(firstNumbers[index])
        secondNumber = int(secondNumbers[index])
        
        # Check if the numbers at the same position are different
        if firstNumber != secondNumber:
            differenceCount += 1

    # Determine if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the program by calling the main function
main()


      1 2 3
      1 2 4
      

      5 6 7
      5 8 7
      

      9 8 7
      5 8 6
      

      1 2 3
      4 5 6
      

      0 0 0
      0 0 0
      