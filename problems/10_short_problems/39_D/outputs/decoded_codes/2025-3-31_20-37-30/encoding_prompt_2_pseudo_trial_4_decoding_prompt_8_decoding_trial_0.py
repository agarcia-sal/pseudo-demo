def main():
    # Step 1: Gather input
    firstInput = input()
    secondInput = input()
    
    # Step 2: Split input into individual components
    firstInputComponents = firstInput.split()
    secondInputComponents = secondInput.split()
    
    # Step 3: Initialize a counter for differences
    differenceCounter = 0
    
    # Step 4: Compare corresponding components from both inputs
    for index in range(3):
        firstValue = int(firstInputComponents[index])
        secondValue = int(secondInputComponents[index])
        
        # If the values are not equal, increment the difference counter
        if firstValue != secondValue:
            differenceCounter += 1
    
    # Step 5: Determine and output the result based on the number of differences
    if differenceCounter < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
