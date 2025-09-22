# Start the process
# Read an integer value `n` from the user, representing the size of an array
n = int(input())

# Initialize an array `isPrime` of size `n` with all values set to `True`
isPrime = [True] * n

# Set a variable `currentIndex` to 0, which will be used to track the position in the array
currentIndex = 0

# Set another variable `step` to 1, which will control the increment for the current index
step = 1

# Begin a loop that continues as long as `step` is less than or equal to 500,000
while step <= 500000:
    # Check if the value at the position `currentIndex` in the array `isPrime` is `True`
    if isPrime[currentIndex]:
        # If it is `True`, change the value at `currentIndex` to `False` (marking it as not prime)
        isPrime[currentIndex] = False
    # Increment the `step` by 1
    step += 1
    # Update `currentIndex` to be the new position calculated
    currentIndex = (currentIndex + step) % n

# Create a new list `untouchedIndices` 
untouchedIndices = [idx for idx, val in enumerate(isPrime) if val]

# Check the length of `untouchedIndices`
if len(untouchedIndices) == 0:
    print("YES")
else:
    print("NO")

# End the process
