# Example of a tuple.
t = 1, 3, 'hello'

# Can be accessed by index.
print('Accessing by index:', t[0])

# Tuples may be nested.
t0 = 1, 2, (1, 'hello', 2)
print('Tuples can be nested', t0)

# Tuples are immutable.
# t[0] = 88 -> ERROR

# Tuples can contain mutable objects.
t1 = [1, 2], 1, (1,3), [3, 'hola']
print('Tuples can contain mutable objects such as lists', t1)

# Creating a empty tuple
empty_tuple = ()
print('The len of empty_tuple:', len(empty_tuple))

# Creating a tuple with one element
singleton = 1,
print('The len of singleton:', len(singleton), 'and its value:', singleton)

# Sequence unpacking
x, y, z = t
print('x value:', x, '\ny value:', y, '\nz value:', z)

print('\n')

list0 = list(range(3))
x, y, z = tuple(list0)
print('x value:', x, '\ny value:', y, '\nz value:', z)

