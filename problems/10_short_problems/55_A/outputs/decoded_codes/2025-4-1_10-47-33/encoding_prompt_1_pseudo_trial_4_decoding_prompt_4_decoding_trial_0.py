def main():
    # Step 1: Input the size of the array
    n = int(input())
    
    # Step 2: Initialize the boolean array
    isTrue = [True] * n  # Create a list of size n with all elements set to True
    
    # Step 3: Set initial variables
    currentIndex = 0
    increment = 1
    
    # Step 4: Loop until increment exceeds 500000
    while increment <= 500000:
        if isTrue[currentIndex]:
            isTrue[currentIndex] = False  # Mark current index as processed
        
        increment += 1  # Increment the counter
        currentIndex = (currentIndex + increment) % n  # Update index with wrap-around
    
    # Step 5: Check remaining True elements
    remainingTrue = [value for value in isTrue if value]
    
    # Step 6: Output result based on remaining True elements
    if len(remainingTrue) == 0:
        print("YES")  # All elements processed
    else:
        print("NO")   # Some elements remain True

# Execute the main function to run the program
if __name__ == "__main__":
    main()
