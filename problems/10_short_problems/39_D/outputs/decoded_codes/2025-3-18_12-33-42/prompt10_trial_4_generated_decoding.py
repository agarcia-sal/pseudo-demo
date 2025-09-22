def main():
    # Step 1: Get two input strings from the user
    string1 = input()
    string2 = input()

    # Step 2: Split the input strings into lists of words
    list1 = string1.split()
    list2 = string2.split()

    # Step 3: Initialize a result counter
    difference_count = 0 

    # Step 4: Loop through the first three elements of both lists
    for i in range(3):
        # Step 5: Convert the elements to integers
        num1 = int(list1[i])
        num2 = int(list2[i])
        
        # Step 6: Compare the two integers
        if num1 != num2:
            # Increment the result counter if they are different
            difference_count += 1 

    # Step 7: Check the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
