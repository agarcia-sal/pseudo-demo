def main():
    # Gather inputs from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of numbers
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a difference counter
    differenceCount = 0 

    # Loop through the first three values of both lists
    for index in range(3):
        # Convert the current values from both lists to integers for comparison
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1 
    
    # Check the number of differences
    if differenceCount < 3:
        print("YES")  # They differ in fewer than three positions
    else:
        print("NO")   # They differ in three or more positions

# Start the program
main()
