def do_main():
    # Read two lines of input
    t1 = input()
    t2 = input()

    # Split the input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()

    # Initialize a variable to count differences
    difference_count = 0

    # Iterate through the three corresponding elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        a = int(tt1[index])
        b = int(tt2[index])

        # If elements are different, increment the difference count
        if a != b:
            difference_count += 1

    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution
do_main()


  1 2 3
  1 2 4
  

  1 2 3
  4 5 6
  

  1 1 1
  1 1 1
  