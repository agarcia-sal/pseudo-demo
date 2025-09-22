def doMain():
    # Read input for the first sequence of values
    input1 = input()
    
    # Read input for the second sequence of values
    input2 = input()
    
    # Split inputs into lists of values
    values1 = input1.split()
    values2 = input2.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Compare corresponding values in each list up to index 2
    for i in range(3):  # Loop from 0 to 2 inclusive
        value1 = int(values1[i])
        value2 = int(values2[i])
        
        # Count differences
        if value1 != value2:
            differenceCount += 1
    
    # Determine the output based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function if the script is run directly
if __name__ == "__main__":
    doMain()
