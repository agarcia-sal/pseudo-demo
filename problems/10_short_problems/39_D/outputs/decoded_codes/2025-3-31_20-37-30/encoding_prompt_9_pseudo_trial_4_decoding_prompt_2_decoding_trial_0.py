def main():
    # Step 1: Receive input for the first set of integers
    print("Enter the first set of integers:")
    firstSet = input()

    # Step 2: Receive input for the second set of integers
    print("Enter the second set of integers:")
    secondSet = input()

    # Step 3: Split the input into individual integers
    firstSetList = firstSet.split()
    secondSetList = secondSet.split()

    # Step 4: Initialize a counter for differences
    differenceCount = 0

    # Step 5: Compare corresponding integers in both sets
    for index in range(3):  # We know we want the first three elements
        # Convert the current string values to integers
        firstValue = int(firstSetList[index])
        secondValue = int(secondSetList[index])
        
        # Step 6: Check if the integers are different
        if firstValue != secondValue:
            differenceCount += 1

    # Step 7: Determine if the two sets are considered similar
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Execute the main function when the script runs
if __name__ == "__main__":
    main()
