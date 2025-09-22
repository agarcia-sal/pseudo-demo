def main():
    # Get input strings representing two sets of three integers
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of integers
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize result counter for differing integers
    differenceCount = 0 
    
    # Compare corresponding integers from both lists
    for index in range(3):
        # Convert elements to integers for comparison
        firstInteger = int(firstList[index])
        secondInteger = int(secondList[index])
        
        # Check if they are different
        if firstInteger != secondInteger:
            differenceCount += 1  # Increment the difference count
    
    # Check the number of differing integers
    if differenceCount < 3:
        print("YES")  # Output "YES" if fewer than 3 integers are different
    else:
        print("NO")   # Output "NO" if 3 or more integers are different

# Entry point of the program
if __name__ == "__main__":
    main()
