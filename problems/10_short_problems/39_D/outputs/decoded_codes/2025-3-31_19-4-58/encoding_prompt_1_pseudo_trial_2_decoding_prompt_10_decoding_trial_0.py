def do_main():
    # Step 1: Input Collection
    input1 = input()
    input2 = input()
    
    # Step 2: Data Processing
    list1 = input1.split()
    list2 = input2.split()
    difference_count = 0

    # Step 3: Comparison Loop
    for index in range(3):
        value_a = int(list1[index])
        value_b = int(list2[index])
        
        # Count the differences between the values
        if value_a != value_b:
            difference_count += 1

    # Step 4: Output Decision
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    do_main()
