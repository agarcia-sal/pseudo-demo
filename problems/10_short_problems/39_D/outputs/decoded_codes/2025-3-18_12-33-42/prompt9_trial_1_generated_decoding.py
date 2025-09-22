def main():
    # Step 1: Get input from the user
    firstSet = []
    secondSet = []
    
    # Prompt user for the first set of three integers
    for i in range(3):
        firstSet.append(int(input()))  # Store the first set

    # Prompt user for the second set of three integers
    for i in range(3):
        secondSet.append(int(input()))  # Store the second set

    # Step 2: Process the input
    difference_counter = 0  # Initialize a difference counter to 0

    # Step 3: Compare the two sets item by item
    for index in range(3):
        firstValue = firstSet[index]  # Value from the first set
        secondValue = secondSet[index]  # Value from the second set
        
        if firstValue != secondValue:  # Compare values
            difference_counter += 1  # Increment the difference counter if they are not equal

    # Step 4: Determine the output based on differences
    if difference_counter < 3:
        print("YES")  # Fewer than 3 differences
    else:
        print("NO")  # 3 or more differences

# To execute the main function
main()
