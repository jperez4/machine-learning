def first_example():
    """Example to show how to iterate over a list"""
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))


def modifying_exercise():
    """Exercise to show how to iterate over a list that you want to modify, using a slice copy"""
    words = ['cat', 'window', 'defenestrate']
    for w in words[:]: # Loop over a slice copy of the entire list.
        if len(w) > 6:
            words.insert(0, w)

    print(words)


def range_exercise():
    """Exercise to show the use of the range function"""
    a = ['Mary', 'had', 'a', 'little', 'lamb']

    print("One after another")
    for i in range(5):
        print(i)

    print("\n")

    print("In steps of 3")
    print(list(range(0, 10, 3)))

    print("\n")

    print("Iterating over the indices of a sequence")
    for i in range(len(a)):  # Better with enumerate(a)
        print(i, a[i])  # print(i)


def break_exercise():
    """Exercise to show the use of the break function"""
    for n in range(2, 5):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # Loop fell through without finding a factor
            print(n, 'is a prime number')


def continue_exercise():
    """Exercise to show the use of the continue function"""
    for n in range(2, 10):
        if n % 2 == 0:
            print(n, 'is an even number')
            continue
        print(n, 'is an odd number')


def pass_exercise():
    """Exercise to show the use of the pass function"""
    def initlog(*args):
        pass  # Remember to implement this!


def ask_execution(prompt, retries=3, reminder='Please select one available option'):
    """Function to select the exercise to run."""
    options = {0: first_example,
               1: modifying_exercise,
               2: range_exercise,
               3: break_exercise,
               4: continue_exercise,
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
