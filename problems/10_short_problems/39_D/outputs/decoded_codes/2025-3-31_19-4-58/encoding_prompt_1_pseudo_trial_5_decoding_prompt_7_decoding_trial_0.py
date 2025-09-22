def main():
    # Read two lines of input for the first and second lists
    firstList = input()
    secondList = input()
    
    # Split the input strings into lists of values
    firstValues = firstList.split()
    secondValues = secondList.split()
    
    # Initialize a counter for the differences
    differenceCount = 0
    
    # Loop through each index 0, 1, 2
    for x in range(3):
        # Convert the current elements of both lists to integers
        valueA = int(firstValues[x])
        valueB = int(secondValues[x])
        
        # Check if the values are different
        if valueA != valueB:
            # Increment the counter if they are different
            differenceCount += 1
            
    # Output "YES" if differences are less than 3, otherwise "NO"
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Invoke the main function when executing the script
if __name__ == "__main__":
    main()
