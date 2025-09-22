def main():
    # Read two lines of input
    firstLine = input()
    secondLine = input()
    
    # Split the input lines into lists of strings
    list1 = firstLine.split()
    list2 = secondLine.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Loop through the index range of the first three elements
    for index in range(3):
        # Convert the current elements to integers
        valueFromFirstLine = int(list1[index])
        valueFromSecondLine = int(list2[index])
        
        # Compare the corresponding values
        if valueFromFirstLine != valueFromSecondLine:
            # Increment the difference counter
            differenceCount += 1
    
    # Check if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")  # There are fewer than 3 differences
    else:
        print("NO")   # There are 3 or more differences

# Execute the main function if this module is run directly
if __name__ == "__main__":
    main()
