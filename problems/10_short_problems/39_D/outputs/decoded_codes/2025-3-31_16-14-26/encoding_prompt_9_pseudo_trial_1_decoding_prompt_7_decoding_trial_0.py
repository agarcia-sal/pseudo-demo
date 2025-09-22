def main():
    # Step 2: Receive Input
    # Prompting the user for the first and second set of integers as strings
    first_input = input()
    second_input = input()
    
    # Step 3: Split Input into Individual Numbers
    # Splitting the input strings into lists of integers
    firstSet = list(map(int, first_input.split()))
    secondSet = list(map(int, second_input.split()))

    # Step 4: Initialize Difference Counter
    differenceCount = 0

    # Step 5: Compare Corresponding Items
    # Loop through indices 0 to 2 for comparison
    for i in range(3):
        firstNumber = firstSet[i]   # First number in firstSet
        secondNumber = secondSet[i]  # Corresponding number in secondSet
        
        # Check if the numbers differ
        if firstNumber != secondNumber:
            differenceCount += 1  # Increment the difference count if they are not equal

    # Step 6: Determine Result Based on Differences
    if differenceCount < 3:
        print("YES")  # Print YES if differences are fewer than 3
    else:
        print("NO")   # Print NO if differences are 3 or more

# Step 7: Execution Trigger
if __name__ == "__main__":
    main()  # Invoke the main function to start the program
