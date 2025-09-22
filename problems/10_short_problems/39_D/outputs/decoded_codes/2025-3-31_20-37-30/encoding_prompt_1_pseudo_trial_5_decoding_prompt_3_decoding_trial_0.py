def doMain():
    # Read the first and second sequences of values
    input1 = input()
    input2 = input()
    
    # Split the inputs into lists of values
    values1 = input1.split()
    values2 = input2.split()
    
    # Initialize a counter for the differences
    differenceCount = 0
    
    # Compare values at corresponding indices
    for i in range(3):  # Loop through indices 0 to 2
        value1 = int(values1[i])  # Convert to integer
        value2 = int(values2[i])  # Convert to integer
        
        # Increment the difference count if values are not equal
        if value1 != value2:
            differenceCount += 1
    
    # Print result based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function if this script is executed directly
if __name__ == "__main__":
    doMain()
