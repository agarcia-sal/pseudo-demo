def main():
    # Step 1: Gather inputs as strings
    firstInput = input()
    secondInput = input()

    # Step 2: Split the input strings into lists of values
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Step 3: Initialize a difference counter
    differenceCount = 0 

    # Step 4: Loop through the first three values of both lists
    for index in range(3):
        # Convert the current values from both lists to integers for comparison
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1 

    # Step 5: Check the number of differences
    if differenceCount < 3:
        print("YES")  # They differ in fewer than three positions
    else:
        print("NO")   # They differ in three or more positions

# Step 6: Start the program
main()
