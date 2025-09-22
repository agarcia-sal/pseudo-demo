def doMain():
    t1 = ""
    t2 = ""
    res = 0

    print("Please enter the first line of numbers:")
    t1 = input()
    print("Please enter the second line of numbers:")
    t2 = input()

    tt1 = t1.split()
    tt2 = t2.split()

    for index in range(3):
        a = int(tt1[index])
        b = int(tt2[index])
        
        if a != b:
            res += 1

    if res < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    doMain()
