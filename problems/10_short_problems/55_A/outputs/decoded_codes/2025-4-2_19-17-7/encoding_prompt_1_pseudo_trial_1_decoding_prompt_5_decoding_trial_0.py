# Function to determine if a list of numbers contains only prime numbers
def check_for_remaining_primes():
    # Step 1: Input the number of elements
    n = int(input())
    
    # Step 2: Initialize a boolean list
    isPrime = [True] * n
    
    # Step 3: Initialize variables
    step = 1       # Represents the current step in our iteration process
    index = 0      # Tracks the current position in the isPrime list

    # Step 4: Loop to iterate a maximum of 500,000 times
    while step <= 500000:
        if isPrime[index]:  # If the value at current index is True
            isPrime[index] = False  # Set it to False
            
        step += 1  # Increment step
        index = (index + step) % n  # Update the index

    # Step 5: Collect remaining True values
    remainingTrue = [value for value in isPrime if value] 

    # Step 6: Check the result
    if not remainingTrue:  # If remainingTrue is empty
        print("YES")
    else:
        print("NO")

# Uncomment the following line to run the function
# check_for_remaining_primes()  
