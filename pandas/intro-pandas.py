import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Core data
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
data = pd.DataFrame({'City_name': city_names, 'Population': population})


def exercise_basic_concepts():
    """Exercise to practise basic concepts of pandas."""
    print("The currently pandas version is:", pd.__version__, "\n")
    print(data, "\n")

    # Getting data from url
    california_housing_data = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv",
                                          sep=",")
    # Prints several statistical values
    print(california_housing_data.describe(), "\n")
    # Prints the first n rows
    print(california_housing_data.head(), "\n")
    # Show histogram of data
    plt.show(california_housing_data.hist('housing_median_age'))


def exercise_accessing_data():
    """Exercise to practise access to the data."""
    print("The result of executing 'exercise_accessing_data' is:")
    print("The data type of the column 'City_name' is:", type(data['City_name']), "\n")
    print("The values of the column 'City_name' are:")
    print(data['City_name'], "\n")
    print("The data type of one data value of the column 'City_name' is:", type(data['City_name'][1]), "\n")
    print("The first data value of the column 'City_name' is:", data['City_name'][1], "\n")
    print("The data type of the first 2 positions of 'data' is:", type(data[0:2]), "\n")
    print("The data value of the first 2 positions of 'data' is:")
    print(data[0:2], "\n")


def exercise_manipulating_data():
    """Exercise to practise data manipulation."""
    print("The result of executing 'exercise_manipulating_data' is:")
    print("The division of the pd.Series population by 1000 is:")
    print((population / 1000), "\n")
    print("The logarithm of the pd.Series population is:")
    print(np.log(population), "\n")
    print("Lambda function applied to pd.Series population:")
    print(population.apply(lambda val: val > 1000000), "\n")
    print("Original dataset:")
    print(data, "\n")

    data['City_name'] = pd.Series(['City1', 'City2', 'City3'])
    area = data['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
    data['Density'] = population / area
    print("Dataset after adding some columns:")
    print(data)


def exercise1():
    """Exercise that adds new columns to the data."""
    print(exercise1.__doc__)
    area = data['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
    data['Boolean'] = city_names.apply(lambda name: "San" in name) & area.apply(lambda val: val > 50)
    print(data)


def exercise_indexes():
    """Exercise that changes the indexes of the data."""
    print(exercise_indexes.__doc__)
    print("The indexes of 'data' are:", data.index)
    print(data, "\n")
    print("Changing the indexes of 'data'")
    print(data.reindex([2, 0, 1]), "\n")
    print("Changing the indexes of 'data' randomly")
    print(data.reindex(np.random.permutation(data.index)))


def exercise2():
    """Exercise that changes the indexes of 'data' with outbound values."""
    print(exercise2.__doc__)
    print(data.reindex([4, 0, 1]))


def ask_execution(prompt, retries=3, reminder='Please select one available option'):
    """Function to select the exercise to run."""
    options = {0: exercise_basic_concepts,
               1: exercise_accessing_data,
               2: exercise_manipulating_data,
               3: exercise1,
               4: exercise_indexes,
               5: exercise2,
               }

    while True:
        print("Select one of the available exercises to run:")
        for i in range(6):
            print("[%i]" % i, options[i].__doc__)

        user_input = int(input(prompt))
        if int(user_input) in range(6):
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
