# Function to compare two sets of three numbers
def compare_number_sets():
    # Step 2: Receive Input
    firstSet = input()
    secondSet = input()
    
    # Step 3: Split Input into Individual Numbers
    firstList = firstSet.split()
    secondList = secondSet.split()

    # Step 4: Initialize a Counter for Differences
    differenceCount = 0

    # Step 5: Compare Each Number in the Sets
    for index in range(3):
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])

        if firstNumber != secondNumber:
            differenceCount += 1  # Increase count if numbers differ

    # Step 6: Determine the Result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 1: Start the Program
compare_number_sets()
