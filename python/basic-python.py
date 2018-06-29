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


default_mutable_object()