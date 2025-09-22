def compare_value_sets():
    # Step 1: Receive Input
    first_set = input()
    second_set = input()
    
    # Step 2: Split Input into Lists
    first_list = first_set.split()
    second_list = second_set.split()
    
    # Step 3: Initialize a Counter
    difference_count = 0
    
    # Step 4: Compare Corresponding Values
    for index in range(3):
        value_from_first = int(first_list[index])
        value_from_second = int(second_list[index])
        if value_from_first != value_from_second:
            difference_count += 1
            
    # Step 5: Evaluate the Result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# To execute the main process
compare_value_sets()
