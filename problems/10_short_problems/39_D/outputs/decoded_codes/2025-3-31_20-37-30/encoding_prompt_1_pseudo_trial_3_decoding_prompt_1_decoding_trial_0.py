def main():
    # Read input values for two sets of triplets
    firstTriplet = input()
    secondTriplet = input()
    
    # Split the input strings into individual components
    aList = firstTriplet.split()
    bList = secondTriplet.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare corresponding elements of the two triplets
    for index in range(3):
        # Convert the string elements to integers for comparison
        firstValue = int(aList[index])
        secondValue = int(bList[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1

    # Determine if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")  # Indicating that the triplet is similar
    else:
        print("NO")   # Indicating that the triplet is not similar

# If the script is executed as the main program, call the main function
if __name__ == "__main__":
    main()
