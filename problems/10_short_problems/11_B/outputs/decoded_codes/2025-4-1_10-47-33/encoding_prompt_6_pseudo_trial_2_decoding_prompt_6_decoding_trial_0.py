# Import the 'abs' function to get absolute values
user_input = input()  # Get input from the user
n = abs(int(user_input))  # Convert the input to an integer and get its absolute value
i = 0  # Initialize an index variable

while True:  # Start an infinite loop
    # Calculate the sum of the first i integers using the formula
    sum_of_first_i = (i * (i + 1)) // 2  # Use integer division
    
    # Calculate the difference between the sum and n
    difference = sum_of_first_i - n
    
    # Check if the sum equals n
    if sum_of_first_i == n:
        print(i)  # Print the value of i
        break  # Exit the loop

    # Check if the sum is greater than n
    elif sum_of_first_i > n:
        # Check if the difference is even
        if difference % 2 == 0:  # Check if 'difference' is even
            print(i)  # Print the value of i
            break  # Exit the loop

    # Increment i for the next iteration
    i += 1
