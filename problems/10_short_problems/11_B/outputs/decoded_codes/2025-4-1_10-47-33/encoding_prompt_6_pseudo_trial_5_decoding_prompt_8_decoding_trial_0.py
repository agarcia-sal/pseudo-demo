# Function to calculate the absolute value
def absolute_value(n):
    return abs(n)

# Function to check if a number is even
def is_even(n):
    return n % 2 == 0

# Main program
number = absolute_value(int(input()))
index = 0

while True:
    # Calculate the sum of the first 'index' natural numbers
    sum_of_natural_numbers = (index * (index + 1)) // 2
    
    # Calculate the difference between the sum and the input number
    difference = sum_of_natural_numbers - number
    
    # Check if the calculated sum matches the input number
    if sum_of_natural_numbers == number:
        print(index)
        break
        
    # Check if the sum has exceeded the input number
    elif sum_of_natural_numbers > number:
        # Check if the difference is even
        if is_even(difference):
            print(index)
            break
            
    # Increment the index for the next iteration
    index += 1
