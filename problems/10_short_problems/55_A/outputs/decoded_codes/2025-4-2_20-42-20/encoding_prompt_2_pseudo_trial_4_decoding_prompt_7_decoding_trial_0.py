# Step 1: Start the process.

# Step 2: Read an integer value 'n' from the user, representing the size of an array.
n = int(input())

# Step 3: Initialize an array 'isPrime' of size 'n' with all values set to 'True'.
isPrime = [True] * n

# Step 4: Set a variable 'currentIndex' to 0.
currentIndex = 0

# Step 5: Set another variable 'step' to 1.
step = 1

# Step 6: Begin a loop that continues as long as 'step' is less than or equal to 500,000.
while step <= 500000:
    # Step 6a: Check if the value at currentIndex in the array isPrime is True.
    if isPrime[currentIndex]:
        # If it is True, change the value at currentIndex to False (marking it as not prime).
        isPrime[currentIndex] = False
    
    # Increment the 'step' by 1.
    step += 1
    
    # Update 'currentIndex' to be the new position using modulo to wrap around.
    currentIndex = (currentIndex + step) % n

# Step 7: Create a new list 'untouchedIndices' of all the values from isPrime that are still True.
untouchedIndices = [index for index, value in enumerate(isPrime) if value]

# Step 8: Check the length of untouchedIndices.
if len(untouchedIndices) == 0:
    # If there are no True values left, print "YES".
    print("YES")
else:
    # Otherwise, print "NO".
    print("NO")

# Step 9: End the process.
