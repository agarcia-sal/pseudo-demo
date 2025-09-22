def main():
    # Step 1: Gather input
    firstInput = input()  # Read first input from user
    secondInput = input()  # Read second input from user
    
    # Step 2: Split input into individual components
    firstInputComponents = firstInput.split()  # Split first input into components
    secondInputComponents = secondInput.split()  # Split second input into components
    
    # Step 3: Initialize a counter for differences
    differenceCounter = 0  # Counter for tracking differences between inputs
    
    # Step 4: Compare corresponding components from both inputs
    for index in range(3):  # We only compare the first three components
        # Convert components to integers for comparison
        firstValue = int(firstInputComponents[index])
        secondValue = int(secondInputComponents[index])
        
        # If the values are not equal, increment the difference counter
        if firstValue != secondValue:
            differenceCounter += 1  # Increment difference counter if values differ
    
    # Step 5: Determine and output the result based on the number of differences
    if differenceCounter < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")  # Output "NO" if differences are 3 or more

# Call the main function to execute the program
main()
