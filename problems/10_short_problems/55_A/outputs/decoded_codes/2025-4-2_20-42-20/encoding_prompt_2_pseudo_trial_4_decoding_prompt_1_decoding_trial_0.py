# 1. Start the process.
# Process starts automatically in Python

# 2. Read an integer value `n` from the user, representing the size of an array.
n = int(input())

# 3. Initialize an array `isPrime` of size `n` with all values set to `True`. 
# This indicates that all positions are initially considered prime.
isPrime = [True] * n

# 4. Set a variable `currentIndex` to 0, which will be used to track the position in the array.
currentIndex = 0

# 5. Set another variable `step` to 1, which will control the increment for the current index.
step = 1

# 6. Begin a loop that continues as long as `step` is less than or equal to 500,000:
while step <= 500000:
    # Check if the value at the position `currentIndex` in the array `isPrime` is `True`.
    if isPrime[currentIndex]:
        # If it is `True`, change the value at `currentIndex` to `False` (marking it as not prime).
        isPrime[currentIndex] = False
        
    # Increment the `step` by 1.
    step += 1
    
    # Update `currentIndex` to be the new position calculated by adding `step` to the current value 
    # of `currentIndex`, and then taking the result modulo `n` to wrap around if necessary.
    currentIndex = (currentIndex + step) % n

# 7. Create a new list `untouchedIndices`, which contains all the values from `isPrime` that remain `True`.
untouchedIndices = [index for index, value in enumerate(isPrime) if value]

# 8. Check the length of `untouchedIndices`:
if len(untouchedIndices) == 0:
    # If there are no `True` values left (i.e., the length is zero), print "YES".
    print("YES")
else:
    # Otherwise, print "NO".
    print("NO")

# 9. End the process.
# Process ends automatically as the script completes.
