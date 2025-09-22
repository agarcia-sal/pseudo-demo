# Begin the main program
# Accept an integer input representing the size of the list
totalNumbers = int(input())  # Read the total number of positions
# Initialize a list of boolean values set to True, indicating potential primes
isPrimeArray = [True] * totalNumbers  

# Initialize variables for tracking positions
positionIncrement = 1         # This will determine how many positions to skip
currentIndex = 0              # The current index in the isPrimeArray

# Process through a range to determine positions marked as non-prime
while positionIncrement <= 500000:  # Loop until positionIncrement exceeds 500000
    # If the current boolean position is still True
    if isPrimeArray[currentIndex]:  
        # Mark this position as False
        isPrimeArray[currentIndex] = False

    # Increment the position increment
    positionIncrement += 1

    # Calculate the next index to mark in a circular manner
    currentIndex = (currentIndex + positionIncrement) % totalNumbers

# Filter the list for positions that are still marked as True
remainingPrimes = [i for i in range(totalNumbers) if isPrimeArray[i]]

# Check if there are any True values remaining
if len(remainingPrimes) == 0:  
    print('YES')  # Indicate that no primes remain
else:
    print('NO')   # Indicate that some primes remain
