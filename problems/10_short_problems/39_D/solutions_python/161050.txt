str1 = input()
str2 = input()

l1 = str1.split(" ")
l2 = str2.split(" ")

yes = "NO"
for i in range(0,3):
	if int(l1[i]) == int(l2[i]):
		yes = "YES"
		
print(yes)
