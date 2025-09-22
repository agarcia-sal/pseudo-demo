def doMain():
    # Read input for the first sequence of values
    input1 = input()
    
    # Read input for the second sequence of values
    input2 = input()
    
    # Split the input strings into lists of values
    values1 = input1.split()
    values2 = input2.split()
    
    # Initialize a counter for the differences
    differenceCount = 0
    
    # Check the first three values for differences
    for i in range(3):
        # Convert values to integers
        value1 = int(values1[i])
        value2 = int(values2[i])
        
        # If the values are different, increment the counter
        if value1 != value2:
            differenceCount += 1
    
    # If there are fewer than 3 differences, print "YES"
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    doMain()
