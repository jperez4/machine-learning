# Create a list of squares
# List comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses. The result will be a new list resulting from evaluating
# the expression in the context of the for and if clauses which follow it.
squares = [x**2 for x in range(5)]
print(squares)

# listcomp combines the elements of two lists if they are not equal.
listcomp = [(x, y) for x in [1, 3, 4] for y in [3, 2, 4] if x != y]
print(listcomp)

# Example
vec = [-4, -2, 0, 2, 4]

# Create a new list with the values doubled.
double = [x*2 for x in vec]
print(double)

# Filter the list to exclude negative numbers.
nonegative = [x for x in vec if x >= 0]
print(nonegative)

# Apply a function to all elements
absolute = [abs(x) for x in vec]
print(absolute)

# Create a list of 2-tuples (number, square).
tuplelist = [(x, x**2) for x in vec]
print(tuplelist)

# Flatten a tuple list.
tupleflatten = [num for elem in tuplelist for num in elem]
print(tupleflatten)

# Flatten a list using a listcomp with two 'for'.
vec2 = [[1, 2, 3], [2, 4, 5]]
result = [num for elem in vec2 for num in elem]
print(result)

# List comprehension to transpose a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[elem[i] for elem in matrix] for i in range(3)]
print(transposed)

# Using the zip function that takes the i element of each iterable and creates a tuple.
# The '*' unpack the arguments (each list of the matrix) and takes the i element of each list.
zipping = list(zip(*matrix))
print('Zip function returning a list of tuples', zipping)
original = [list(elem) for elem in zipping]
print('Converting to a list of lists', original)
