def MainProgram():
    # Step 1: Read two lines of input
    firstSet = input()
    secondSet = input()

    # Step 2: Split the input strings into lists of numbers
    listFirst = firstSet.split()
    listSecond = secondSet.split()

    # Step 3: Initialize a counter for differences
    differenceCount = 0 

    # Step 4: Compare each number in the two lists
    for index in range(3):  # since there are 3 numbers
        # Convert the current numbers from strings to integers
        numberFromFirst = int(listFirst[index])
        numberFromSecond = int(listSecond[index])

        # Check if the numbers are different
        if numberFromFirst != numberFromSecond:
            # Increment the difference counter
            differenceCount += 1 

    # Step 5: Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")   # Less than three differences
    else:
        print("NO")    # Three or more differences

# Step 6: Execute the main program
if __name__ == "__main__":  # Check if this file is being run as the main program
    MainProgram()
