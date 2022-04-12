from heapq import merge

dictionary1 = {'Tony': 41, 'Steve': 39, 'Nat': 35}
dictionary2 = {'Bruce': 41, 'Clint': 35, 'Thor': 38}
merged_dictionary = {**dictionary1,**dictionary2}

print("{:<10} {:<10}".format('Name', 'Age'))

for x,y in merged_dictionary.items():
    print("{:<10} {:<10}".format(x,y))

print("-------------")
del merged_dictionary['Nat']

print("{:<10} {:<10}".format('Name', 'Age'))
for x,y in merged_dictionary.items():
    print("{:<10} {:<10}".format(x,y))

print("-------------")
print("{:<10} {:<10}".format('Name', 'Age'))
for i in sorted (merged_dictionary):
    print ("{:<10} {:<10}".format(i, merged_dictionary[i]))

print()
print("Minimum value is: ",min(merged_dictionary.values()))
print("Maximum value is: ",max(merged_dictionary.values()))