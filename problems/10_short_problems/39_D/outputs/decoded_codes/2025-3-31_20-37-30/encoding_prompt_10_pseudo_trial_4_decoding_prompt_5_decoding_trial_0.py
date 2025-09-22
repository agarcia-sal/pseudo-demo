def do_main():
    # Step 1: Take two inputs
    input1 = input()
    input2 = input()

    # Step 2: Split inputs into lists of strings
    list1 = input1.split()
    list2 = input2.split()

    # Step 3: Initialize a result counter
    result_counter = 0 

    # Step 4: Loop through the first three elements of the lists
    for index in range(3):
        # Convert string elements to integers
        num1 = int(list1[index])
        num2 = int(list2[index])
        
        # Step 5: Compare the numbers and update the counter
        if num1 != num2:
            result_counter += 1 

    # Step 6: Check the result counter
    if result_counter < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the do_main function if this script is run as the main program
if __name__ == "__main__":
    do_main()
