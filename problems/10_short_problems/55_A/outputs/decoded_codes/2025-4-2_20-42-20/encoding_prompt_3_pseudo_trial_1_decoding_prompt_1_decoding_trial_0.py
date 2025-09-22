# Read an integer input that specifies the size of array
n = int(input())

# Initialize a boolean array with size n, setting all values to True
isPrime = [True] * n

# Initialize index variables
indexIncrement = 0
currentIndex = 1

# Loop until currentIndex exceeds 500,000
while currentIndex <= 500000:
    # If the value at currentIndex is True, mark it as False (indicating elimination)
    if indexIncrement < n and isPrime[indexIncrement]:
        isPrime[indexIncrement] = False

    # Move to the next increment
    currentIndex += 1
    
    # Update indexIncrement using a wrapping technique based on n
    indexIncrement = (indexIncrement + currentIndex) % n

# Create a new list of values that are still marked True in the isPrime array
nonEliminatedValues = [value for value in isPrime if value]

# Check if there are any remaining True values in the nonEliminatedValues list
if len(nonEliminatedValues) == 0:
    print('YES')  # Output indicates all values were eliminated
else:
    print('NO')   # Output indicates some values remained
