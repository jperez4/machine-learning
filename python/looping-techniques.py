# When looping through dictionaries, the key and the value can be retrieved at the same time with
# the items() method.
print("Looping through dictionaries")
knights = dict(gallahad="the pure", robin="the brave")
for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding value can be retrived
# at the same time using enumerate() function.
print("\nLooping through sequences")
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can be paired with the zip function.
questions = ['name', 'quest']
answers = ['lancelot', 'the holy grail']
print("\nZipping two sequences")
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

# To loop over a sequence in reverse
print("\nLooping through a sequence in reverse")
for i in reversed(range(1, 10, 2)):
    print(i)

# To loop over a sequence in sorted order, the function leaves the source unaltered
basket = ['apple', 'orange', 'pear', 'banana']
print("\nLooping through a sorted list")
for i in sorted(basket):
    print(i)
