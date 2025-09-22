def do_main():
    # Step 1: Read input strings
    input_str1 = input()
    input_str2 = input()

    # Step 2: Split input strings into lists
    list1 = input_str1.split()
    list2 = input_str2.split()

    # Step 3: Initialize a variable to count differences
    difference_count = 0

    # Step 4: Loop through the first three elements of the lists
    for i in range(3):
        # Step 5: Convert string elements to integers
        num1 = int(list1[i])
        num2 = int(list2[i])
        
        # Step 6: Compare the values and increment difference count if not equal
        if num1 != num2:
            difference_count += 1
    
    # Step 7: Check the number of differences and print the result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Execute the main function when the script runs
if __name__ == "__main__":
    do_main()
