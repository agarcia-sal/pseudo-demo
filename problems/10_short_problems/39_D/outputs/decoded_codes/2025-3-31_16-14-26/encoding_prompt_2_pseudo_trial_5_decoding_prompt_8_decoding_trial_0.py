def main():
    inputString1 = input()
    inputString2 = input()
    
    tokens1 = inputString1.split()
    tokens2 = inputString2.split()
    
    differenceCount = 0
    
    for index in range(3):
        valueFromFirstInput = int(tokens1[index])
        valueFromSecondInput = int(tokens2[index])
        
        if valueFromFirstInput != valueFromSecondInput:
            differenceCount += 1
    
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
