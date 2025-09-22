# Start

# Input: Read an integer value from the user and take its absolute value.
targetNumber = abs(int(input()))

# Initialize: Set a variable "index" to 0.
index = 0

# Loop: Begin an infinite loop.
while True:
    # Calculate the sum "currentSum" as the sum of the first "index" natural numbers.
    currentSum = (index * (index + 1)) // 2
    
    # Calculate a difference "difference".
    difference = currentSum - targetNumber

    # Conditions:
    if currentSum == targetNumber:
        print(index)  # Print the value of "index".
        break  # Exit the loop.
        
    elif currentSum > targetNumber:
        if difference % 2 == 0:  # Check if "difference" is an even number.
            print(index)  # Print the value of "index".
            break  # Exit the loop.
    
    # Update: Increment the "index" by 1.
    index += 1

# End


def find_index_for_target_number(targetNumber):
    targetNumber = abs(targetNumber)  # ensure non-negative
    index = 0
    while True:
        currentSum = (index * (index + 1)) // 2
        difference = currentSum - targetNumber
        
        if currentSum == targetNumber:
            return index  # Found exact match
        elif currentSum > targetNumber and difference % 2 == 0:
            return index  # Found feasible index
        
        index += 1

# usage
input_value = int(input())
result = find_index_for_target_number(input_value)
print(result)
