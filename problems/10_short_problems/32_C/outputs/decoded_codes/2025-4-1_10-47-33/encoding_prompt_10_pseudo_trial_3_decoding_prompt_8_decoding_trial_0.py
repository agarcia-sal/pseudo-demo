def mc(n, s):
    q, r = divmod(n, s)
    
    if r > 0:
        return r * (q + 1)
    else:
        return n

n = int(input())
m = int(input())
s = int(input())

result = mc(n, s) * mc(m, s)
print(result)


     def get_input():
         return int(input()), int(input()), int(input())
     