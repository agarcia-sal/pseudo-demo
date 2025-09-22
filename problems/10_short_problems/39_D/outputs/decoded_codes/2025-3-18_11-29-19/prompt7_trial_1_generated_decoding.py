def main():
    # Read two input strings representing triplet values
    inputString1 = input()
    inputString2 = input()
    
    # Split the input strings into lists of values
    listOfValues1 = inputString1.split()
    listOfValues2 = inputString2.split()
    
    # Initialize a variable to count differences
    differenceCount = 0 
    
    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert the current values to integers for comparison
        value1 = int(listOfValues1[index])
        value2 = int(listOfValues2[index])
        
        # Check if the values are different
        if value1 != value2:
            # Increment difference count if values are different
            differenceCount += 1 
    
    # Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
