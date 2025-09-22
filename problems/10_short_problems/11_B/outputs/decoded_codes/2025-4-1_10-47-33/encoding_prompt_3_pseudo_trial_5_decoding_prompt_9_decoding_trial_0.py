# Read an integer input from the user and convert it to absolute value
user_input = abs(int(input()))
index = 0

# Infinite loop to find the required index
while True:
    # Calculate the sum of the first 'index' natural numbers
    total_sum = (index * (index + 1)) // 2
    
    # Calculate the difference from the user input
    difference = total_sum - user_input
    
    # Check if we found the desired sum
    if total_sum == user_input:
        print(index)
        break
    
    # If sum is greater than user input
    elif total_sum > user_input:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)
            break
    
    # Increment index for the next iteration
    index += 1
