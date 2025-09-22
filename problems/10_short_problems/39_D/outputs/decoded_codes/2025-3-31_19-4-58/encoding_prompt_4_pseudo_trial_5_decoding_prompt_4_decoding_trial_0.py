def do_main():
    # Read two strings of input
    t1 = input()
    t2 = input()

    # Split the input strings into lists of words
    tt1 = t1.split()
    tt2 = t2.split()

    # Initialize a counter for differences
    res = 0 

    # Loop through the first three elements of both lists
    for x in range(3):
        # Convert the corresponding elements to integers
        a = int(tt1[x])
        b = int(tt2[x])

        # If the numbers are not the same, increment the difference counter
        if a != b:
            res += 1 

    # Check if the number of differences is less than 3
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    do_main()


   "1 2 3"
   "1 2 3"
   

   "1 2 4"
   "1 2 5"
   

   "5 6 2"
   "1 2 3"
   

   "7 8 9"
   "7 8 10"
   