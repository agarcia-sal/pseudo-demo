# Get Input
targetSum = abs(int(input()))

# Initialize Counter
currentIndex = 0

# Loop Indefinitely
while True:
    # Calculate Sum
    currentSum = currentIndex * (currentIndex + 1) // 2  # Use integer division
    
    # Difference Calculation
    difference = currentSum - targetSum

    # Check for Exact Match
    if currentSum == targetSum:
        print(currentIndex)
        break

    # Check for Overshoot
    if currentSum > targetSum:
        if difference % 2 == 0:
            print(currentIndex)
            break

    # Increment Index
    currentIndex += 1


def find_smallest_integer(target):
    targetSum = abs(target)
    currentIndex = 0

    while True:
        currentSum = currentIndex * (currentIndex + 1) // 2
        difference = currentSum - targetSum

        if currentSum == targetSum:
            return currentIndex

        if currentSum > targetSum:
            if difference % 2 == 0:
                return currentIndex

        currentIndex += 1

# Get Input
user_input = int(input())
result = find_smallest_integer(user_input)
print(result)
