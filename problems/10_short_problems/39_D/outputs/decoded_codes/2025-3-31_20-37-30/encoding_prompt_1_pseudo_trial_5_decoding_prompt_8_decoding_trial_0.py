def doMain():
    input1 = input()
    input2 = input()
    
    values1 = input1.split()
    values2 = input2.split()
    
    differenceCount = 0
    
    for i in range(3):  # Loop through indices 0 to 2
        value1 = int(values1[i])
        value2 = int(values2[i])
        
        if value1 != value2:
            differenceCount += 1
            
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    doMain()
