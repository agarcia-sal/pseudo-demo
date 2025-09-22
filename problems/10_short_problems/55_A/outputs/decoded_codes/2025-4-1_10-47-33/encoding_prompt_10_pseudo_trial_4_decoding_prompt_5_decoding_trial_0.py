def process_boolean_list():
    # Step 1: Input Handling
    n = int(input())
    
    # Step 2: Initialize a boolean list b
    boolean_list = [True] * n
    j = 0
    i = 1

    # Step 3: Loop to modify the boolean list
    while i <= 500000:
        if boolean_list[j]:  # If the current index is True
            boolean_list[j] = False  # Set it to False
            
        # Step 4: Increment i and update j
        i += 1  # Increment i
        j = (j + i) % n  # Update j with modulo n

    # Step 5: Extract remaining TRUE values from boolean_list
    remaining_true_values = [val for val in boolean_list if val]

    # Step 6: Check the result and print output
    if len(remaining_true_values) == 0:
        print('YES')
    else:
        print('NO')

# Example of how to call the function (uncomment to test):
# process_boolean_list()
