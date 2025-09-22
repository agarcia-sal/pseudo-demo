# Get input from the user
n = int(input())  # Size of the list

# Initialize the list to track visited positions, all set to True initially
isVisited = [True] * n

# Initialize the current position index and the step count
currentIndex = 0
stepCount = 1

# Mark visited positions
while stepCount <= 500000:
    if isVisited[currentIndex] == True:
        isVisited[currentIndex] = False  # Mark this position as visited
    
    stepCount += 1  # Increment the step count
    currentIndex = (currentIndex + stepCount) % n  # Update the current index

# Check remaining unvisited positions
remainingTrue = [value for value in isVisited if value == True]  # Collect all unvisited positions

# Output result based on the presence of unvisited positions
if len(remainingTrue) == 0:
    print("YES")  # All positions have been visited
else:
    print("NO")   # Some positions are still unvisited
