def main():
    # 2. Obtain the first set of input values from the user
    firstInput = input()
    
    # 3. Obtain the second set of input values from the user
    secondInput = input()
    
    # 4. Split firstInput into a list of values
    firstValues = firstInput.split()
    
    # 5. Split secondInput into a list of values
    secondValues = secondInput.split()
    
    # 6. Initialize discrepancyCount to zero
    discrepancyCount = 0
    
    # 7. For each index from 0 to 2
    for i in range(3):
        # - Convert values at the current index to integers
        valueFromFirst = int(firstValues[i])
        valueFromSecond = int(secondValues[i])
        
        # - Compare the two values
        if valueFromFirst != valueFromSecond:
            # - If not equal, increment discrepancyCount
            discrepancyCount += 1
            
    # 8. Evaluate discrepancyCount
    if discrepancyCount < 3:
        print("YES")
    else:
        print("NO")

# 9. End the main process
main()
