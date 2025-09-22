def do_main():
    # Read two lines of input from the user
    input1 = input()
    input2 = input()

    # Split the input strings into lists of substrings
    list1 = input1.split()
    list2 = input2.split()
    
    # Initialize the result counter
    differences_count = 0

    # Iterate over the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        value1 = int(list1[index])
        value2 = int(list2[index])

        # Check if the values are different
        if value1 != value2:
            differences_count += 1

    # Determine if the number of differences is less than three
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
do_main()


  1 2 3
  1 2 4
  

  YES
  

  5 6 7
  5 6 7
  

  NO
  

  10 20 30
  10 25 30
  

  YES
  