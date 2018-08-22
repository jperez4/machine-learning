def defining_and_calling_functions():
    """Exercise that define and call functions."""
    print(defining_and_calling_functions.__doc__)

    def fib(n):
        """Print Fibonacci series up to n."""
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
        print()

    fib(2000)
    # Documentation Strings
    print(fib.__doc__)
    # Function renaming mechanism
    f = fib
    f(100)

    def fib2(n):
        """Return a list containing the Fibonacci series up to n."""
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a + b
        return result

    f100 = fib2(100)
    print(f100)


def default_argument_values():
    """Exercise to practise with default argument values in functions."""
    def ask_ok(prompt, retries=4, reminder='Please try again!'):
        """Function to test how to specify default values for one or more arguments."""
        while True:
            ok = input(prompt)
            if ok in ('y', 'ye', 'yes'):
                return True
            if ok in ('n', 'no', 'nop', 'nope'):
                return False
            retries = retries - 1
            if retries < 0:
                raise ValueError('invalid user response')
            print(reminder)

    # Calling with only the mandatory argument
    # ask_ok('Do you really want to quit?')
    # Giving one of the optional arguments
    # ask_ok('OK to overwrite the file?', 2)
    print(ask_ok.__doc__)
    ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


def default_mutable_object():
    """Exercise to show how a function works with a mutable default objects."""
    def f(a, list_object=[]):
        """Subsequent calls add the value."""
        list_object.append(a)
        return list_object

    print(f.__doc__)
    print(f(1))
    print(f(2))
    print(f(3), "\n")

    def f1(a, list_object=None):
        """The default value is not shared between subsequent calls."""
        if list_object is None:
            list_object = []
        list_object.append(a)
        return list_object

    print(f1.__doc__)
    print(f1(1))
    print(f1(2))
    print(f1(3))


def keyword_arguments():
    """Exercise to practise with keyword arguments."""
    def parrot(voltage, state='a stiff', action='voom'):
        print("The action is", action, end='\n')
        print("The voltage is", voltage, end='\n')
        print("The state is", state, end='\n')

    # Valid calls
    parrot(1000)
    print('\n')
    parrot(voltage=1000)
    print('\n')
    parrot(action='NO', voltage=1000)
    print('\n')
    parrot(1000, state='Open')

    # Invalid calls
    # parrot()  # Required argument missing
    # parrot(10, voltage=100)  # Duplicate value for same argument
    # Non-keyword argument after a keyword argument
    # parrot(voltage=100, 'Closed')


def keyword_arguments_advanced():
    """Exercise to practise with keyword arguments making use of Tuples and Dictionaries."""
    def cheeseshop(kind, *arguments, **keywords):
        print("-- Do you have any", kind, "?")
        print("-- I'm sorry, we're all out of", kind)
        for arg in arguments:
            print(arg)
        print("-" * 40)
        for kw in keywords:
            print(kw, ":", keywords[kw])

    cheeseshop("Apple", "Sorry,sir", "I'm really sorry",
               shoopkeeper="Michael", client="George")
    print('\n')

    # Calling with unpacked argument lists
    dict = {"shoopkeeper": "Michael", "client": "George"}
    tuple = ("Sorry,sir", "I'm really sorry")

    cheeseshop("Apple", *tuple, **dict)
    print('\n')

    def concat(*args, sep='/'):
        """Concatenation of the argument followed by a slash."""
        return sep.join(args)

    print(concat.__doc__)
    print(concat("Mercury", "Venus", "Earth"))


def ask_execution(prompt, retries=3, reminder='Please select one available option'):
    """Function to select the exercise to run."""
    options = {0: defining_and_calling_functions,
               1: default_argument_values,
               2: default_mutable_object,
               3: keyword_arguments,
               4: keyword_arguments_advanced,
               }

    while True:
        print("Select one of the available exercises to run:")
        for i in range(5):
            print("[%i]" % i, options[i].__doc__)

        user_input = int(input(prompt))
        if int(user_input) in range(5):
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

