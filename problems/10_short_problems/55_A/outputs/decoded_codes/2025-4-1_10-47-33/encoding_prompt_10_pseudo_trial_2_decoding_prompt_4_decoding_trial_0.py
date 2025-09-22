def main():
    # Step 1: Input integer value n
    n = int(input())

    # Step 2: Initialize a list of boolean values
    boolean_list = [True] * n

    # Step 3: Initialize variables
    index_to_check = 0
    increment_value = 1

    # Step 4: Loop until increment_value exceeds 500000
    while increment_value <= 500000:
        # Step 5: Check if the current index in boolean_list is True
        if boolean_list[index_to_check]:
            # Step 6: Set the current index to False
            boolean_list[index_to_check] = False

        # Step 7: Increment increment_value
        increment_value += 1
        
        # Step 8: Update index_to_check to the next index in a circular manner
        index_to_check = (index_to_check + increment_value) % n

    # Step 9: Create a list x containing all True values in boolean_list
    true_values = [value for value in boolean_list if value]

    # Step 10: Check if there are no True values in x
    if len(true_values) == 0:
        # Step 11: Print 'YES' if no True values exist
        print('YES')
    else:
        # Step 12: Print 'NO' if True values exist
        print('NO')

if __name__ == "__main__":
    main()
