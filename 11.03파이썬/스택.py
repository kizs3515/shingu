a = [1,2,3,4,5]
a.append(10)
a.append(20)
print a.pop()
print a.pop()

a = ['s','h','i','n','g','u']

i = 0
while i < 6:
   print a.pop(),
   i += 1
print ""
b = "Shingu University"
c = list(b)

for i in range(len(c)):
    print c.pop(0),
    
