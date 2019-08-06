import copy

a=[[1,2,3,4],[4,5,6,7]]

b=copy.deepcopy(a)

print("a and b before modify")

print(a)

print(b)

a[0][1]=10

print("a and b after modify. b was obtain as a copy of a")

print(a)

print(b)