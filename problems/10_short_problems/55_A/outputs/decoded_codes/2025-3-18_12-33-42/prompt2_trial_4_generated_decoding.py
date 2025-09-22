# Step 1: Input
n = int(input())

# Step 2: Initialize List
isPrimeCandidate = [True] * n

# Step 3: Set Starting Index and Increment
currentIndex = 0
incrementValue = 1

# Step 4: Outer Loop for Operations
while incrementValue <= 500000:
    if isPrimeCandidate[currentIndex]:  # Check if the candidate is still True
        isPrimeCandidate[currentIndex] = False  # Set it to False
    
    incrementValue += 1  # Increase incrementValue by 1
    currentIndex = (currentIndex + incrementValue) % n  # Update currentIndex circularly

# Step 5: Identify Remaining True Values
remainingTrueValues = [i for i, is_prime in enumerate(isPrimeCandidate) if is_prime]

# Step 6: Output Check
if not remainingTrueValues:  # If remainingTrueValues is empty
    print('YES')
else:
    print('NO')
