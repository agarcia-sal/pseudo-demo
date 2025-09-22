def doMain():
    # Step 2: Receive Input
    firstSet = input()
    secondSet = input()
    
    # Step 3: Split the Input into lists
    listFirst = firstSet.split()
    listSecond = secondSet.split()

    # Step 4: Initialize Difference Counter
    differenceCount = 0
    
    # Step 5: Compare the Numbers
    for index in range(3):  # Loop through indices 0 to 2
        # Convert the numbers to integers
        numberFromFirst = int(listFirst[index])
        numberFromSecond = int(listSecond[index])
        
        # Check if the numbers differ
        if numberFromFirst != numberFromSecond:
            differenceCount += 1

    # Step 6: Check Differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the Function
if __name__ == "__main__":
    doMain()
