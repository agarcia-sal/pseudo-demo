def do_main():
    # Read input values from the user
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize the result counter
    res = 0
    
    # Compare the elements of the lists
    for x in range(3):  # We expect exactly three elements to compare
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Increment result if elements differ
        if a != b:
            res += 1

    # Determine the result based on the comparison count
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main program execution
do_main()


   Input:
   "1 2 3"
   "1 2 3"
   Output: "YES"

   Input:
   "1 2 3"
   "4 5 6"
   Output: "NO"

   Input:
   "1 2 3"
   "1 2 4"
   Output: "YES"
   

   Input:
   "0 0 0"
   "0 0 0"
   Output: "YES"

   Input:
   "100 200 300"
   "100 200 400"
   Output: "YES"

   Input:
   "5 4 3"
   "7 8 9"
   Output: "NO"
   