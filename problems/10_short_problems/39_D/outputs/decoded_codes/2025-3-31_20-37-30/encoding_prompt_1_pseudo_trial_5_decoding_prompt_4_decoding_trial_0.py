def doMain():
    # Read input for the first sequence of values
    input1 = input()
    
    # Read input for the second sequence of values
    input2 = input()
    
    # Split input into lists of values
    values1 = input1.split()
    values2 = input2.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Iterate through the indices of the lists
    for i in range(3):
        # Convert the string values to integers
        value1 = int(values1[i])
        value2 = int(values2[i])
        
        # Check for differences between the two sequences
        if value1 != value2:
            differenceCount += 1
    
    # Determine the output based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function if this script is executed directly
if __name__ == "__main__":
    doMain()
