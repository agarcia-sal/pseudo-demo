def main():
    # Read input values
    firstString = input()
    secondString = input()
    
    # Split the input strings into lists
    firstList = firstString.split()
    secondList = secondString.split()
    
    # Initialize a mismatch counter
    mismatchCount = 0 
    
    # Compare the first three elements of both lists
    for index in range(3):
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # If the values do not match, increment the mismatch counter
        if firstValue != secondValue:
            mismatchCount += 1
    
    # Check the number of mismatches and print the result
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
