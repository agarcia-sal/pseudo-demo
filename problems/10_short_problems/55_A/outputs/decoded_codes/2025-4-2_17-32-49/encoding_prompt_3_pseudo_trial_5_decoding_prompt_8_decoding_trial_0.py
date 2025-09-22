# Accept an integer input representing the size of the list
totalNumbers = int(input())
isPrimeArray = [True] * totalNumbers

# Initialize variables for tracking positions
positionIncrement = 1
currentIndex = 0

# Process through a range to determine prime-like positions
while positionIncrement <= 500000:
    
    # If the current boolean position is still True
    if isPrimeArray[currentIndex] is True:
        
        # Mark this position as False
        isPrimeArray[currentIndex] = False

    # Increment the position increment
    positionIncrement += 1

    # Calculate the next index to mark in a circular manner
    currentIndex = (currentIndex + positionIncrement) % totalNumbers

# Filter the list for positions that are still marked as True
remainingPrimes = [value for value in isPrimeArray if value]

# Check if there are any True values remaining
if len(remainingPrimes) == 0:
    print('YES')  # Indicate that no primes remain
else:
    print('NO')   # Indicate that some primes remain
