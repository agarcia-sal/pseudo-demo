def do_main():
    # Step 1: Read two lines of input and store them in variables
    t1 = input().strip()  # First input string
    t2 = input().strip()  # Second input string

    # Step 2: Split the input strings into lists of substrings
    tt1 = t1.split()  # Splitting the first input string
    tt2 = t2.split()  # Splitting the second input string

    # Step 3: Initialize a variable to count differences
    difference_count = 0 

    # Step 4: Compare elements of the two lists
    for index in range(3):  # We expect both lists to have at least 3 elements
        # Convert the substring to an integer for comparison
        a = int(tt1[index])
        b = int(tt2[index])

        # Step 5: Increment the count if the numbers are not equal
        if a != b:
            difference_count += 1  # Increment difference count if they are not equal

    # Step 6: Determine output based on the number of differences
    if difference_count < 3:
        print("YES")  # Fewer than 3 differences
    else:
        print("NO")   # 3 or more differences

# Step 7: Main execution block
if __name__ == "__main__":
    do_main()


  1 2 3
  1 2 3
  

  1 2 3
  4 5 6
  

  1 2 3
  1 3 2
  