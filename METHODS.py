tuple_a = (1,2,3)
x = tuple_a._hash_()
print(x)

tuple_b = (1,2,3)
y = tuple_b._hash_()
print(y)

tuple_c = (1,2,3)
z = tuple_c._hash_()
print(z)

dict_a = {}
dict_a[tuple_a] = "sahhasj"
print(dict_a[tuple_a])
print(dict_a[tuple_c])

f = id(x) == id(y)
print(f)

f = x._hash() == z.hash_()
print(f)