def dictionaries_exercise():
    """Exercise to practise with python dictionaries and the operations overt them."""
    # Creating a dictionary
    tel = {'jack': 4098, 'sape': 4139}

    # Adding a pair
    tel['guido'] = 4127

    # Printing the dictionary
    print("The pairs contained in the dictionary are: \n", tel)

    # Getting the value associated to a key
    print("The value associated to 'jack' is:", tel['jack'])

    # Deleting a pair
    del tel['sape']
    print("The situation of the dictionary after deleting 'sape': \n", tel)

    # Retrieve the keys of the dictionary in a list
    print("The keys of the dictionary are: \n", list(tel))

    # Retrieve the keys of the dictionary in a sorted list
    print("The keys of the dictionary  sorted are: \n", sorted(tel))

    # Check if a key exists in a dictionary
    print("Check if 'guido' exists in the dictionary:", 'guido' in tel)

    # The dict() constructor builds dictionaries directly from sequences of key-value pairs
    print("Create a dict from sequences of key-value pairs: \n", dict([('sape', 432), ('guido', 321)]))

    # Creating a dictionary from arbitrary key-value expressions
    ran = {x: x**2 for x in (2, 4, 6)}
    print("Creating a dictionary from an expression: \n", ran)

    # When the keys are simple string, it is sometimes easier to specify pair using keyword arguments
    print("Creating a dict using keyword arguments: \n", dict(sape=21, guido=43))


def list_exercise():
    """Exercise to practise with lists"""
    squares = [1, 4, 9, 16, 25]
    print("Indexing returns the item", squares[0])
    print("Indexing with negative values", squares[-1])
    print("Slicing returns a new list", squares[-3:])
    print("Lists also support concatenation: \n", squares + [3, 432, 45, 32])
    print("Lists are mutable objects, before modifying and appending: \n", squares)
    squares[2] = 34
    squares.append(323)
    print("After: \n", squares)

    print('\n')

    print("Lists can change by slicing too")
    letters = ['a', 'b', 'c', 'd']
    print("List before: \n", letters)
    letters[2:4] = ['C', 'D']
    print("List after: \n", letters)
    print("Items can be remove by slicing")
    letters[2:4] = []
    print(letters)
    print("Or you can remove the entire list")
    letters[:] = []
    print(letters)
    print("The len function also applies to lists, the len of the list is:", len(letters))
    print("Is it possible to nest list")
    a = [[1, 3], ['a', 'c']]
    print(a, a[0], a[1])


def set_exercise():
    """Exercise to practise with set structure"""
    basket = {'apple', 'orange', 'apple', 'banana', 'orange'}
    print("Duplicated items from set have been removed: \n", basket)
    print("You can perform a fast membership testing: is orange in basket?:", 'orange' in basket)
    print("Set comprehensions are also supported")
    a = {x for x in 'muscle' if x not in 'mcl'}
    print(a)


def ask_execution(prompt, retries=3, reminder='Please select one available option'):
    """Function to select the exercise to run."""
    options = {0: dictionaries_exercise,
               1: list_exercise,
               2: set_exercise,
               }

    while True:
        print("Select one of the available exercises to run:")
        for i in range(3):
            print("[%i]" % i, options[i].__doc__)

        user_input = int(input(prompt))
        if int(user_input) in range(3):
            options[user_input]()
            user_input = input("New execution?:")
            if user_input in ('y', 'ye', 'yes'):
                pass
            elif user_input in ('n', 'no', 'nop', 'nope'):
                return False
            else:
                raise ValueError("invalid user response: must be 'yes' or 'no'")
        else:
            print("The chosen it's invalid")
            retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)


ask_execution('Enter your option:')
