# Start

# Input: Read an integer value from the user and take its absolute value
targetNumber = abs(int(input()))

# Initialize: Set a variable "index" to 0
index = 0

# Loop: Begin an infinite loop
while True:
    # Calculate the sum "currentSum" using the formula
    currentSum = (index * (index + 1)) // 2

    # Calculate difference
    difference = currentSum - targetNumber

    # Conditions:
    if currentSum == targetNumber:
        print(index)  # Print the value of "index"
        break  # Exit the loop
    
    elif currentSum > targetNumber:
        # Check if "difference" is an even number
        if difference % 2 == 0:
            print(index)  # Print the value of "index"
            break  # Exit the loop
    
    # Update: Increment the "index" by 1
    index += 1

# End
