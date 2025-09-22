n = abs(int(input()))
i = 0

while True:
    s = (i * (i + 1)) // 2
    m = s - n
    
    if s == n:
        print(i)
        break
    
    elif s > n:
        if m % 2 == 0:
            print(i)
            break
    
    i += 1


def find_sum_index(n):
    n = abs(n)
    i = 0

    while True:
        s = (i * (i + 1)) // 2
        m = s - n
    
        if s == n:
            return i
        
        elif s > n:
            if m % 2 == 0:
                return i
        
        i += 1

# Sample Input/Output
n = int(input())
print(find_sum_index(n))
