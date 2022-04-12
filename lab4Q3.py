dictionary = {}
for x in range(1,31,1):
    dictionary[x]=x*x

print(dictionary)
print()

for x,y in dictionary.items():
    print(x,y)

sum = 0
for x,y in dictionary.items():
    sum = sum + y
print()
print("sum: ")
print(sum)
print()

del dictionary[10]

print(dictionary)