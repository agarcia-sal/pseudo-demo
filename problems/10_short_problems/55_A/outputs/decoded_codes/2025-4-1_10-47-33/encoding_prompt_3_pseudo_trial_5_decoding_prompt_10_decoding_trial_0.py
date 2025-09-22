def main():
    # Step 1: Read an integer value 'n' from user
    n = int(input())
    
    # Step 2: Initialize a boolean list 'b' of size 'n' with all values set to True
    boolean_list = [True] * n
    
    # Step 3: Initialize variables
    index_j = 0  # Acts as an index for the list 'b'
    counter_i = 1  # This counter will increment in the loop

    # Step 4: Loop to perform operations while 'counter_i' is less than or equal to 500000
    while counter_i <= 500000:
        # Step 4.1: Check if the current index 'index_j' in the list 'boolean_list' is True
        if boolean_list[index_j]:
            # Step 4.2: Set the current index 'index_j' to False
            boolean_list[index_j] = False

        # Step 4.3: Increment 'counter_i' by 1
        counter_i += 1
        
        # Step 4.4: Update index 'index_j' with the modulo operation
        index_j = (index_j + counter_i) % n

    # Step 5: Filter the list 'boolean_list' to collect all elements that are still True
    filtered_list = [value for value in boolean_list if value]

    # Step 6: Check if the filtered list is empty and output accordingly
    if not filtered_list:
        print('YES')
    else:
        print('NO')

# Entry point of the program
if __name__ == '__main__':
    main()
