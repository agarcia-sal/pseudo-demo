def main():
    # Step 1: Accept user input for two lines of numbers
    t1 = input()
    t2 = input()

    # Step 2: Split the input lines into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare each pair of numbers
    for index in range(3):  # Expecting exactly 3 pairs
        # Step 4a: Convert the strings to integers for comparison
        number1 = int(tt1[index])
        number2 = int(tt2[index])

        # Step 4b: Check if the two numbers differ
        if number1 != number2:
            difference_count += 1
    
    # Step 5: Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")  # The pairs differ in less than three positions
    else:
        print("NO")   # The pairs differ in three or more positions

# Execute the main function when the program starts
if __name__ == "__main__":
    main()


   1 2 3
   1 2 4
   

   5 6 7
   5 6 7
   

   8 9 10
   8 9 11
   

   4 5 6
   7 8 9
   

   1 2 3
   4 5 6
   