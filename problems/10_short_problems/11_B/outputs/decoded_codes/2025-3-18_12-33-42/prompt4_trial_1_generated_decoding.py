def absolute_value_of_integer_input():
    # Prompt user for input and convert to an absolute integer
    return abs(int(input()))

def sum_of_first_i_natural_numbers(i):
    # Calculate sum of the first i natural numbers using the formula
    return (i * (i + 1)) // 2  # Use integer division

def is_even(number):
    # Check if the provided number is even
    return number % 2 == 0

def find_natural_number_for_sum():
    # Read an integer input and take its absolute value
    n = absolute_value_of_integer_input()

    # Initialize a counter variable
    i = 0

    # Infinite loop to find the solution
    while True:
        # Calculate the sum of the first i natural numbers
        sum_i = sum_of_first_i_natural_numbers(i)

        # Calculate the difference between sum_i and n
        difference = sum_i - n

        # Check if the sum is equal to n
        if sum_i == n:
            print(i)  # Output i if the sum matches n
            break

        # Check if the sum exceeds n
        elif sum_i > n:
            # Check if the difference is even
            if is_even(difference):
                print(i)  # Output i if the difference is even
                break

        # Increment the counter variable
        i += 1

# Execute the function to run the code
find_natural_number_for_sum()
