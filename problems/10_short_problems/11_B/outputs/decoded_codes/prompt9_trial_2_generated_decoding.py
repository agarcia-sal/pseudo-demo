# Start of the algorithm
input_number = abs(int(input()))  # Read input from the user and convert it to absolute value
index = 0  # Initialize the index to track natural numbers

while True:  # Repeat indefinitely
    sum_value = (index * (index + 1)) // 2  # Calculate the sum of the first 'index' natural numbers
    difference = sum_value - input_number  # Calculate the difference between sum and input number
    
    if sum_value == input_number:  # Check if the sum matches the input number
        print(index)  # Print the index where the sum equals the input number
        break  # Exit the loop
    elif sum_value > input_number:  # Check if the sum exceeds the input number
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Print the index where the sum exceeds the input number by an even difference
            break  # Exit the loop

    index += 1  # Increment the index to check the next natural number
