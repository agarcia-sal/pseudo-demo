def absolute_value_of(num):
    """
    Function to return the absolute value of a given number.
    """
    if num < 0:
        return -num
    return num

def sum_of_first_i_numbers(i):
    """
    Function to calculate the sum of the first i natural numbers using the formula:
    sum = i * (i + 1) / 2
    """
    return (i * (i + 1)) // 2  # Using integer division

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
        break  # Exit the loop
    
    # Check if the sum exceeds n
    elif s > n:
        # Check if the difference m is even
        if m % 2 == 0:
            print(i)  # Print the current number i
            break  # Exit the loop
    
    # Increment i for the next iteration
    i += 1

# Test cases can be added below as comments:
# print(absolute_value_of(-5))  # Expected: 5
# print(sum_of_first_i_numbers(5))  # Expected: 15 (1+2+3+4+5)
