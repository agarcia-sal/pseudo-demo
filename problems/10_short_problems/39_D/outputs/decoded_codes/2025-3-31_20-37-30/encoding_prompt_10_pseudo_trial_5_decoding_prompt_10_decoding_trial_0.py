def do_main():
    # Step 1: Read two lines of input
    input1 = input()
    input2 = input()

    # Step 2: Split the input strings into lists of strings
    list1 = input1.split()
    list2 = input2.split()
    
    # Step 3: Initialize a count for differences
    difference_count = 0

    # Step 4: Compare corresponding elements in the two lists
    for i in range(3):
        # Step 4a: Convert string elements to integers
        num1 = int(list1[i])
        num2 = int(list2[i])

        # Step 4b: Check for differences
        if num1 != num2:
            difference_count += 1

    # Step 5: Check the count of differences and output the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main Execution Block
if __name__ == "__main__":
    do_main()
