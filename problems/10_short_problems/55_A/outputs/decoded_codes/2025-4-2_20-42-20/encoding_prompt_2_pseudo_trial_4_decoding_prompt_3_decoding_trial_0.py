def main():
    # Step 1: Start the process
    # Step 2: Read an integer value n
    n = int(input())
    
    # Step 3: Initialize an array isPrime of size n with all values set to True
    isPrime = [True] * n
    
    # Step 4: Set a variable currentIndex to 0
    currentIndex = 0
    
    # Step 5: Set another variable step to 1
    step = 1
    
    # Step 6: Begin a loop that continues as long as step <= 500,000
    while step <= 500000:
        # Step 6.1: Check if isPrime[currentIndex] is True
        if isPrime[currentIndex]:
            # Step 6.1.1: Change the value at currentIndex to False
            isPrime[currentIndex] = False
            
        # Step 6.2: Increment the step by 1
        step += 1
        
        # Step 6.3: Update currentIndex
        currentIndex = (currentIndex + step) % n
    
    # Step 7: Create untouchedIndices with all values from isPrime that are still True
    untouchedIndices = [index for index, prime in enumerate(isPrime) if prime]
    
    # Step 8: Check the length of untouchedIndices
    if len(untouchedIndices) == 0:
        print("YES")
    else:
        print("NO")
    
    # Step 9: End the process

# Run the main function
main()
