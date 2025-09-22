# Step 1: Read the integer input n that represents the size of the array.
n = int(input())

# Step 2: Initialize the array 'isAlive' with True values indicating all are initially alive.
isAlive = [True] * n

# Initialize variables: currentIndex and stepCount
currentIndex = 0
stepCount = 1

# Step 3: Loop until stepCount exceeds 500000
while stepCount <= 500000:
    # If the current person is alive 
    if isAlive[currentIndex]:
        # Mark that person as eliminated (False)
        isAlive[currentIndex] = False
        
    # Increment the step count by 1 for the next iteration
    stepCount += 1
   
    # Update the currentIndex using stepCount and wrap around using modulus
    currentIndex = (currentIndex + stepCount) % n

# Step 4: Create a list 'remaining' containing all still alive (True) values
remaining = [person for person in isAlive if person]

# Step 5: Check if anyone is still alive and output the results
if len(remaining) == 0:
    print("YES")  # No one is alive
else:
    print("NO")   # There are still people alive
