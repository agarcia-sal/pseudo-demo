s = input().strip()  # Read a line of input and remove any surrounding whitespace

i = 0
ans = ''

while i < len(s):
    if s[i] == '.':
        ans += '0'
        i += 1
    elif i + 1 < len(s) and s[i + 1] == '.':
        ans += '1'
        i += 2
    else:
        ans += '2'
        i += 2

print(ans)


   def encode_string(s):
       ...
   