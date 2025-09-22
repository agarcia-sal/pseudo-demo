# Start the process
# Step 2
n = int(input())  # Read an integer value n from the user, representing the size of an array

# Step 3
isPrime = [True] * n  # Initialize an array isPrime of size n with all values set to True

# Step 4
currentIndex = 0  # Set a variable currentIndex to 0

# Step 5
step = 1  # Set another variable step to 1

# Step 6
while step <= 500000:  # Begin a loop that continues as long as step is less than or equal to 500,000
    if isPrime[currentIndex]:  # Check if the value at currentIndex in the array is True
        isPrime[currentIndex] = False  # Mark it as not prime if it is True
    
    step += 1  # Increment the step by 1
    
    # Update currentIndex
    currentIndex = (currentIndex + step) % n  # Calculate new currentIndex with wrap around using modulo n

# Step 7
untouchedIndices = [i for i in range(n) if isPrime[i]]  # Create a new list containing untouched indices

# Step 8
if len(untouchedIndices) == 0:  # Check the length of untouchedIndices
    print("YES")  # If there are no True values left, print "YES"
else:
    print("NO")  # Otherwise, print "NO"

# Step 9
# End the process
