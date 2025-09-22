def do_main():
    # Step 1: Gather Input
    input1 = input()
    input2 = input()

    # Step 2: Split Inputs into Lists
    list1 = input1.split()
    list2 = input2.split()

    # Step 3: Initialize a Result Counter
    result_counter = 0

    # Step 4: Compare Elements of Both Lists
    for index in range(3):  # Loop through the first three elements
        # Convert current elements to integers
        value_from_list1 = int(list1[index])
        value_from_list2 = int(list2[index])
        
        # Step 5: Check if the values are different
        if value_from_list1 != value_from_list2:
            result_counter += 1

    # Step 6: Determine the Result
    if result_counter < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the Main Function
do_main()
