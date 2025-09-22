def main():
    # Step 2: Receive Input
    firstInput = input()  # Get the first input string from user
    secondInput = input()  # Get the second input string from user

    # Step 3: Split Inputs
    firstList = firstInput.split()  # Split the first input string into a list
    secondList = secondInput.split()  # Split the second input string into a list

    # Step 4: Initialize Difference Counter
    differenceCount = 0  # Initialize count of differences

    # Step 5: Compare Corresponding Elements
    for index in range(3):  # Iterate from index 0 to 2
        firstValue = int(firstList[index])  # Convert element from firstList to integer
        secondValue = int(secondList[index])  # Convert element from secondList to integer
        
        if firstValue != secondValue:  # If values are not equal
            differenceCount += 1  # Increment the difference count

    # Step 6: Determine Output
    if differenceCount < 3:  # If there are less than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Step 7: Execute Main Function
if __name__ == "__main__":
    main()  # Call the main function when the script is executed
