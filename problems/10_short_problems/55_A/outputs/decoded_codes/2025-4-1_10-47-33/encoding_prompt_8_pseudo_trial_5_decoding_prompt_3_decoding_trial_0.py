def main():
    # Step 1: Get user input
    totalCount = int(input())
    
    # Step 2: Initialize the list
    isMarked = [True] * totalCount
    
    # Step 3: Set counters
    currentStep = 1
    index = 0
    
    # Step 4: Processing loop
    while currentStep <= 500000:
        if isMarked[index]:
            isMarked[index] = False  # Mark this position as processed
            
        currentStep += 1
        index = (index + currentStep) % totalCount  # Wrap around to the beginning if needed
        
    # Step 5: Check results
    remainingTrue = [mark for mark in isMarked if mark]
    
    # Step 6: Determine output
    if len(remainingTrue) == 0:
        print("YES")
    else:
        print("NO")

# Run the program
main()
