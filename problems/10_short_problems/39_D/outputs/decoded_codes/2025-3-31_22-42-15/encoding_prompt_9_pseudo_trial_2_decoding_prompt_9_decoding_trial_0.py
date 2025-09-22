def doMain():
    # Receive Input
    firstSet = input()
    secondSet = input()
    
    # Split the Input into lists
    listFirst = firstSet.split()
    listSecond = secondSet.split()
    
    # Initialize Difference Counter
    differenceCount = 0
    
    # Compare the Numbers
    for i in range(3):  # Loop through indices 0, 1, 2
        numberFromFirst = int(listFirst[i])  # Convert to integer
        numberFromSecond = int(listSecond[i])  # Convert to integer
        
        # Check if the numbers differ
        if numberFromFirst != numberFromSecond:
            differenceCount += 1  # Increment the count of differences

    # Check Differences
    if differenceCount < 3:
        print("YES")  # Output "YES" if fewer than 3 differences
    else:
        print("NO")  # Output "NO" if 3 or more differences

# Execute the Function
if __name__ == "__main__":
    doMain()
