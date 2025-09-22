def doMain():
    # Receive input for the first set of three numbers
    firstSet = input()  
    # Receive input for the second set of three numbers
    secondSet = input()  
    
    # Split the input strings into lists of individual numbers
    listFirst = firstSet.split()
    listSecond = secondSet.split()
    
    # Initialize a counter for the number of differences
    differenceCount = 0
    
    # Compare the numbers at each index from 0 to 2
    for index in range(3):
        numberFromFirst = int(listFirst[index])  # Convert number from first list to integer
        numberFromSecond = int(listSecond[index])  # Convert number from second list to integer
        
        # Check if the numbers differ
        if numberFromFirst != numberFromSecond:
            differenceCount += 1  # Increment the difference count
            
    # Check the number of differences and output the result
    if differenceCount < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")  # Output "NO" if differences are 3 or more

# Execute the function if the script is run directly
if __name__ == "__main__":
    doMain()
