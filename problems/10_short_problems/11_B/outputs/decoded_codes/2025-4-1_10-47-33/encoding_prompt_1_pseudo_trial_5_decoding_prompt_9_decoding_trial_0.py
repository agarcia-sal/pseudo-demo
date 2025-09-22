# Read an integer value from the user
user_input = int(input())
# Calculate the absolute value of the input
targetNumber = abs(user_input)

# Initialize the counter variable
index = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first 'index' natural numbers
    currentSum = index * (index + 1) // 2  # Using integer division for accuracy
    # Calculate the difference between currentSum and targetNumber
    difference = currentSum - targetNumber
    
    # Check Conditions
    if currentSum == targetNumber:
        print(index)  # Print the value of index
        break  # Exit the loop
    elif currentSum > targetNumber:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Print the value of index
            break  # Exit the loop
            
    # Increment the value of index by 1
    index += 1
