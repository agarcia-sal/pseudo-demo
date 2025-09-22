# Check Values in a List
def main():
    # Step 2: Read an integer value `n` from user input
    n = int(input())
    
    # Step 3: Create a list `isActive` of length `n`, all elements initially True
    isActive = [True] * n
    
    # Step 4: Initialize variable `currentIndex` to 0
    currentIndex = 0
    
    # Step 5: Initialize variable `increment` to 1
    increment = 1
    
    # Step 6: While `increment` <= 500000
    while increment <= 500000:
        # Step 6.1: If the element at `currentIndex` in `isActive` is True
        if isActive[currentIndex]:
            # Set it to False
            isActive[currentIndex] = False
        
        # Step 6.2: Increment `increment`
        increment += 1
        
        # Step 6.3: Update `currentIndex`
        currentIndex = (currentIndex + increment) % n
    
    # Step 7: Create a list `activeElements` that contains only True elements from `isActive`
    activeElements = [value for value in isActive if value]
    
    # Step 8: If length of `activeElements` is 0
    if len(activeElements) == 0:
        # Output "YES"
        print("YES")
    else:
        # Step 9: Otherwise, output "NO"
        print("NO")

# There is an optional inline check to execute the main function when this script is run
if __name__ == "__main__":
    main()
