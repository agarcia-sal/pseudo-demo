def main():
    # Step 1: Input the size of the array
    size_of_array = int(input())
    
    # Step 2: Initialize a list of boolean values
    is_true = [True] * size_of_array

    # Step 3: Initialize counters
    index = 0
    step = 1

    # Step 4: Loop until step exceeds 500000
    while step <= 500000:
        # Step 4a: Check the current index in the boolean list
        if is_true[index]:
            # Step 4b: Mark the current index as False
            is_true[index] = False
        
        # Step 4c: Increment step
        step += 1
        
        # Step 4d: Calculate the next index using circular arithmetic
        index = (index + step) % size_of_array
    
    # Step 5: Filter the list to find remaining True values
    remaining_true_values = [value for value in is_true if value]

    # Step 6: Check if there are any True values left
    if len(remaining_true_values) == 0:
        # Step 6a: If no True values are left, print 'YES'
        print('YES')
    else:
        # Step 6b: If there are True values left, print 'NO'
        print('NO')

# Run the main function
main()
