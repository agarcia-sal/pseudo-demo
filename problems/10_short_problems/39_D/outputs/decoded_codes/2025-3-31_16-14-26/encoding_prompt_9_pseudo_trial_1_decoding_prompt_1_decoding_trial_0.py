def main():
    # Step 2: Receive Input
    first_input = input()  # First set of three integers
    second_input = input()  # Second set of three integers

    # Step 3: Split Input into Individual Numbers
    firstSet = list(map(int, first_input.split()))  # Convert first input string to list of integers
    secondSet = list(map(int, second_input.split()))  # Convert second input string to list of integers

    # Step 4: Initialize Difference Counter
    differenceCount = 0

    # Step 5: Compare Corresponding Items
    for i in range(3):  # Loop through indices 0 to 2 (for three integers)
        firstNumber = firstSet[i]  # Retrieve first integer
        secondNumber = secondSet[i]  # Retrieve second integer
        
        # Check if the numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1  # Increase count if they differ

    # Step 6: Determine Result Based on Differences
    if differenceCount < 3:  # Check if differences are fewer than 3
        print("YES")  # Output YES if true
    else:
        print("NO")  # Output NO if false

# Step 7: End Main Function
main()  # Trigger the main function
