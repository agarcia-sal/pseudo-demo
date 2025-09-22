# Function to calculate the sum of the first i natural numbers
def sum_of_first_i_numbers(i):
    return (i * (i + 1)) // 2  # Using integer division for accuracy

# Function to get the absolute value of the input integer
def absolute_value_of(num):
    if num < 0:
        return -num
    return num

# Start by taking the absolute value of user input and convert it to an integer
n = absolute_value_of(int(input()))

# Initialize a variable to keep track of the current number
i = 0

# Start an infinite loop for finding the required number
while True:
    # Calculate the sum of the first i natural numbers
    s = sum_of_first_i_numbers(i)
    
    # Determine how much s exceeds n
    m = s - n
    
    # Check if the sum equals n
    if s == n:
        print(i)  # Print the current number i
        break  # Stop the loop
    
    # Check if the sum exceeds n
    elif s > n:
        # Check if the difference m is even
        if m % 2 == 0:
            print(i)  # Print the current number i
            break  # Stop the loop
    
    # Increment i for the next iteration
    i += 1
