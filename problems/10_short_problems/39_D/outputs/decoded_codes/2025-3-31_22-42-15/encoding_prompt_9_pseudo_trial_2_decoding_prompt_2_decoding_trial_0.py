def doMain():
    # Step 2: Receive Input
    firstSet = input()
    secondSet = input()
    
    # Step 3: Split the Input
    listFirst = firstSet.split()
    listSecond = secondSet.split()
    
    # Step 4: Initialize Difference Counter
    differenceCount = 0
    
    # Step 5: Compare the Numbers
    for i in range(3):  # Loop through indices 0, 1, 2
        numberFromFirst = int(listFirst[i])  # Convert to integer
        numberFromSecond = int(listSecond[i])  # Convert to integer
        
        # Compare the two numbers
        if numberFromFirst != numberFromSecond:
            differenceCount += 1  # Increment count on difference
    
    # Step 6: Check Differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the Function
if __name__ == "__main__":
    doMain()
