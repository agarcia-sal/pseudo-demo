def main():
    # Read two lines of input from the user
    firstSet = input()
    secondSet = input()
    
    # Split the input strings into lists of values
    firstValues = firstSet.split()
    secondValues = secondSet.split()
    
    # Initialize a counter to track differences
    differenceCount = 0
    
    # Compare each corresponding value in the two lists
    for index in range(3):  # We assume the input always has at least 3 elements
        # Convert the string values to integers
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            # Increment the difference count
            differenceCount += 1
            
    # Check the total number of differences
    if differenceCount < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# The main block to run the function
if __name__ == "__main__":
    main()
