def main():
    # Step 1: Read input from the user
    t1 = input()  # first string input
    t2 = input()  # second string input

    # Step 2: Split the input strings into lists of words
    tt1 = t1.split()  # list of words from first input
    tt2 = t2.split()  # list of words from second input

    # Step 3: Initialize a variable to count differences
    difference_count = 0 

    # Step 4: Compare corresponding elements in both lists
    for index in range(3):  # assuming both lists have at least 3 elements
        # Convert the current elements to integers
        value_a = int(tt1[index])  
        value_b = int(tt2[index])  

        # Step 5: Check if the values are different
        if value_a != value_b:
            difference_count += 1  # Increment differenceCount by 1 

    # Step 6: Determine and print if differences are less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function
