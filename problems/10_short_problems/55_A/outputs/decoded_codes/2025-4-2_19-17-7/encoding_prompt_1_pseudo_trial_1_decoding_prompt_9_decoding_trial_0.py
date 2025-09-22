# Read the number of elements from the user
n = int(input())

# Initialize a boolean list where all elements are True
isPrime = [True] * n

# Initialize variables
step = 1
index = 0

# Loop to iterate a maximum of 500,000 times
while step <= 500000:
    if isPrime[index]:  # Check if the current index in isPrime is True
        isPrime[index] = False  # Set the position in isPrime to False
    step += 1  # Increment the step
    index = (index + step) % n  # Update index using the formula

# Collect remaining True values
remainingTrue = [value for value in isPrime if value]

# Check the result and output accordingly
if not remainingTrue:  # If the list is empty
    print("YES")
else:
    print("NO")
