def main():
    # Step 2: Receive Input
    firstInput = input()  # Get the first input string
    secondInput = input()  # Get the second input string

    # Step 3: Split Inputs
    firstList = firstInput.split()  # Split the first input string into a list
    secondList = secondInput.split()  # Split the second input string into a list

    # Step 4: Initialize Difference Counter
    differenceCount = 0  

    # Step 5: Compare Corresponding Elements
    for index in range(3):  # Loop through indices 0 to 2
        firstValue = int(firstList[index])  # Convert to int
        secondValue = int(secondList[index])  # Convert to int

        # Check if the values are different
        if firstValue != secondValue:  
            differenceCount += 1  # Increment difference count if values are not equal

    # Step 6: Determine Output
    if differenceCount < 3:  
        print("YES")  # Output if differences are less than 3
    else:
        print("NO")  # Output if 3 or more differences

# Step 7: Execute Main Function
if __name__ == "__main__":  
    main()
