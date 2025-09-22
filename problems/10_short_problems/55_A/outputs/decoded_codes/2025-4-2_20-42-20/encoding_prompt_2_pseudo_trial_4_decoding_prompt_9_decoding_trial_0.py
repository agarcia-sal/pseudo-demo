# Start the process
n = int(input())  # Read an integer value from the user representing the size of an array
isPrime = [True] * n  # Initialize an array of size n with all values set to True
currentIndex = 0  # Variable to track the current index in the array
step = 1  # Variable to control the increment for the current index

# Loop that continues as long as step is less than or equal to 500000
while step <= 500000:
    if isPrime[currentIndex]:  # Check if the value at currentIndex is True
        isPrime[currentIndex] = False  # Mark it as not prime by changing it to False
    
    step += 1  # Increment the step
    currentIndex = (currentIndex + step) % n  # Update currentIndex, wrapping around using modulo n

# Create a new list that contains all the indices that remain True
untouchedIndices = [index for index, is_prime in enumerate(isPrime) if is_prime]

# Check the length of untouchedIndices
if len(untouchedIndices) == 0:  # If there are no True values left
    print("YES")  # Print YES if all values were marked as not prime
else:
    print("NO")  # Print NO if there are values that remain True
