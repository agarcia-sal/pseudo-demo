def main():
    # Input
    n = int(input())
    
    # Initialize
    status = [True] * n
    currentStep = 1
    index = 0
    
    # Loop
    while currentStep <= 500000:
        if status[index]:
            status[index] = False
        
        currentStep += 1
        index = (index + currentStep) % n
    
    # Filter Active Status
    activeElements = [s for s in status if s]
    
    # Check Result
    if len(activeElements) == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
