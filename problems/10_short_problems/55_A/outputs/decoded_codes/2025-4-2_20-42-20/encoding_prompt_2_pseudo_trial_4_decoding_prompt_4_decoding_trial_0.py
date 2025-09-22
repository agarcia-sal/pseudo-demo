def main():
    # Step 1: Read input for the size of the array
    n = int(input())
    
    # Step 2: Initialize the isPrime array with True
    isPrime = [True] * n
    
    # Step 3: Initialize currentIndex and step
    currentIndex = 0
    step = 1
    
    # Step 4: Loop until step is less than or equal to 500,000
    while step <= 500000:
        # Step 5: Check if the currentIndex in isPrime is True
        if isPrime[currentIndex]:
            # Mark currentIndex as not prime
            isPrime[currentIndex] = False
        
        # Increment step and update currentIndex
        step += 1
        currentIndex = (currentIndex + step) % n  # Wrap around using modulo
    
    # Step 6: Collect untouched indices (those still marked as True)
    untouchedIndices = [index for index, value in enumerate(isPrime) if value]
    
    # Step 7: Check the length of untouchedIndices and print the result
    if len(untouchedIndices) == 0:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the process
if __name__ == "__main__":
    main()
