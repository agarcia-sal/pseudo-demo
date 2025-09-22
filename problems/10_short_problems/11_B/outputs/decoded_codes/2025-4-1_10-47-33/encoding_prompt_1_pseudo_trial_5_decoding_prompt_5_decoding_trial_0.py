# This program finds the first integer index such that the sum of the first index natural numbers
# either equals or can be adjusted to equal the absolute value of a given input number.

# Read an integer value from the user
user_input = int(input())
# Calculate the absolute value of the input
target_number = abs(user_input)

# Initialize a counter variable
index = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first index natural numbers
    current_sum = index * (index + 1) // 2
    
    # Calculate the difference between currentSum and targetNumber
    difference = current_sum - target_number
    
    # Check conditions
    if current_sum == target_number:
        print(index)
        break
    elif current_sum > target_number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)
            break
    
    # Increment the value of index by 1
    index += 1
