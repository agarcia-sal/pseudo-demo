def find_smallest_integer(target_number):
    # Ensure the target number is non-negative
    target_number = abs(target_number)
    current_integer = 0

    while True:
        # Calculate the sum of the first `current_integer` natural numbers
        sum_of_integers = current_integer * (current_integer + 1) // 2
        difference = sum_of_integers - target_number
        
        # Check if the sum of integers matches or exceeds the target number by an even amount
        if sum_of_integers == target_number or (difference > 0 and difference % 2 == 0):
            return current_integer
        
        # Increment `current_integer` for the next iteration
        current_integer += 1

# Read input from the user
user_input = int(input())
result = find_smallest_integer(user_input)
print(result)
