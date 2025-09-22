def main():
    # Read an integer input that specifies the size of the array
    n = int(input())
    
    # Initialize a boolean array with size n, all initialized to True
    is_prime = [True] * n

    # Initialize index variables
    index_increment = 0
    current_index = 1

    # Loop until current_index exceeds 500,000
    while current_index <= 500000:
        # If the value at current_index % n is True, mark it as False (indicating elimination)
        if is_prime[index_increment]:
            is_prime[index_increment] = False

        # Move to the next increment
        current_index += 1
        # Update indexIncrement using a wrapping technique based on n
        index_increment = (index_increment + current_index) % n

    # Create a new list of values that are still marked True in the isPrime array
    non_eliminated_values = [value for value in is_prime if value]

    # Check if there are any remaining True values in the nonEliminatedValues list
    if len(non_eliminated_values) == 0:
        print('YES')  # Output indicates all values were eliminated
    else:
        print('NO')   # Output indicates some values remained

# Ensure the main function runs
if __name__ == "__main__":
    main()
