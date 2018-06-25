import tensorflow as tf


def simple_tensorflow_program():
    # Create a graph
    g = tf.Graph()

    # Establish the graph as the "default" graph
    # The session will run the default graph
    with g.as_default(), tf.Session():
        # Assemble a graph consisting of the following three operations:
        #   * Two tf.constant operations to create the operands.
        #   * One tf.add operation to add two operands
        x = tf.constant(8, name="x_const")
        y = tf.constant(2, name="y_const")
        my_sum = tf.add(x, y, name="x_y_sum")

        print("The result of executing 'simple_tensorflow_program' is:")
        print("The sum of", x.eval(), "and", y.eval(), "is", my_sum.eval())


def exercise_third_operand():
    # Create a graph
    g = tf.Graph()

    # Establish the graph as the "default" graph
    # The session will run the default graph
    with g.as_default(), tf.Session():
        # Assemble a graph consisting of the following three operations:
        # (Creating a tensor is an operation)
        #   * Two tf.constant operations to create the operands.
        #   * One tf.add operation to add two operands
        x = tf.constant(8, name="x_const")
        y = tf.constant(5, name="y_const")
        z = tf.constant(4, name="z_const")
        my_sum = tf.add_n([x, y, z], name="x_y_Z_sum")

        print("The result of executing 'exercise_third_operand' is:")
        print("The sum of", x.eval(), ",", y.eval(), "and", z.eval(), "is", my_sum.eval())


def exercise_vector_addition():
    # Create a graph
    g = tf.Graph()

    with g.as_default(), tf.Session():
        # Create a six-element vector (1-D tensor)
        primes = tf.constant([2, 3, 5, 7, 11, 13], dtype=tf.int32)

        # Create another six-element vector. Each element in the
        # vector will be initialized to 1. The first argument is
        # the shape of the tensor
        ones = tf.ones([6], dtype=tf.int32)

        # Add the two vectors. The resulting tensor is a six-element vector
        my_sum = tf.add(primes, ones)

        # Create a session to run the default graph
        print("The result of executing 'exercise_vector_addition' is:")
        print("The sum of", primes.eval(), "and", ones.eval(), "is", my_sum.eval())


def exercise_tensor_shapes():
    # Create a graph
    g = tf.Graph()

    with g.as_default(), tf.Session():
        # A scalar (0-D tensor)
        scalar = tf.zeros([], dtype=tf.int32)
        # A vector with 3 elements
        vector = tf.zeros([3], dtype=tf.int32)
        # A matrix with 2 rows and 3 columns
        matrix = tf.zeros([2, 3], dtype=tf.int32)

        print("The result of executing 'exercise_tensor_shapes' is:")
        print('scalar has shape', scalar.get_shape(), 'and value:\n', scalar.eval(), "\n")
        print('vector has shape', vector.get_shape(), 'and value:\n', vector.eval(), "\n")
        print('matrix has shape', matrix.get_shape(), 'and value:\n', matrix.eval(), "\n")


def exercise_broadcasting():
    # Create a graph
    g = tf.Graph()

    with g.as_default(), tf.Session():
        # Create a six-element vector (1-D vector)
        vector = tf.constant([2, 3, 5, 7, 11, 13], dtype=tf.int32)

        # Create a constant scalar with value 1
        scalar = tf.constant(1, dtype=tf.int32)

        # Add the two tensors. The resulting tensor is a six-element vector
        my_sum = tf.add(vector, scalar)

        print("The result of executing 'exercise_broadcasting' is:")
        print("The sum of", vector.eval(), "and", scalar.eval(), "is", my_sum.eval())


def exercise_matrix_multiplication():
    # Create a graph
    g = tf.Graph()

    with g.as_default(), tf.Session():
        # Create a matrix (2-D tensor) with 3 rows and 4 columns
        x = tf.constant([[5, 2, 4, 3], [5, 1, 6, -2], [-1, 3, -1, -2]],
                        dtype=tf.int32)

        # Create a matrix with 4 rows and 2 columns
        y = tf.constant([[2, 2], [3, 5], [4, 5], [1, 6]], dtype=tf.int32)

        # Multiply 'x' by 'y'
        # The resulting matrix will have 3 rows and 2 columns
        multiply_result = tf.matmul(x, y)

        print("The result of executing 'exercise_matrix_multiplication' is:")
        print("The multiplication of\n", x.eval(), "\nby\n", y.eval(), "\nis\n", multiply_result.eval(), "\n")
        print("The result matrix has shape", multiply_result.get_shape())


def exercise_tensor_reshaping():
    # Create a graph
    g = tf.Graph()

    with g.as_default(), tf.Session():
        # Create an 8x2 matrix (2-D tensor)
        matrix = tf.constant([[1, 2], [3, 4], [5, 6], [7, 8],
                              [9, 10], [11, 12], [13, 14], [15, 16]],
                             dtype=tf.int32)

        # Reshape the 8x2 matrix into a 2x8 matrix
        reshaped_2x8_matrix = tf.reshape(matrix, [2, 8])

        # Reshape the 8x2 matrix into a 4x4 matrix
        reshaped_4x4_matrix = tf.reshape(matrix, [4, 4])

        print("The result of executing 'exercise_tensor_reshaping' is:")
        print("Original matrix (8x2):")
        print(matrix.eval(), "\n")
        print("Reshaped matrix (2x8):")
        print(reshaped_2x8_matrix.eval(), "\n")
        print("Reshaped matrix (4x4):")
        print(reshaped_4x4_matrix.eval(), "\n")

        # Reshape the 8x2 matrix into a 3-D 2x2x4 tensor
        reshaped_2x2x4_tensor = tf.reshape(matrix, [2, 2, 4])

        # Reshape the 8x2 matrix into a 1-D 16-element tensor
        one_dimensional_vector = tf.reshape(matrix, [16])

        print("Original matrix (8x2):")
        print(matrix.eval(), "\n")
        print("Reshaped 3-D tensor (2x2x4):")
        print(reshaped_2x2x4_tensor.eval(), "\n")
        print("1-D vector:")
        print(one_dimensional_vector.eval())


def exercise1():
    # Reshape two tensors in order to multiply them
    # Create a graph
    g = tf.Graph()

    with g.as_default(), tf.Session():
        a = tf.constant([5, 3, 2, 7, 1, 4])  # 1x6
        b = tf.constant([4, 6, 3])  # 1x3

        reshaped_6x1_tensor = tf.reshape(a, [6, 1])
        reshaped_1x3_tensor = tf.reshape(b, [1, 3])

        multiply_result = tf.matmul(reshaped_6x1_tensor, reshaped_1x3_tensor)

        print("The result of executing 'exercise1' is:")
        print("Reshaped tensor (6x1):")
        print(reshaped_6x1_tensor.eval(), "\n")
        print("Reshaped tensor (1x3):")
        print(reshaped_1x3_tensor.eval(), "\n")
        print("Multiply result (6x3):")
        print("The multiplication of\n", reshaped_6x1_tensor.eval(), "\nby\n",
              reshaped_1x3_tensor.eval(), "\nis\n", multiply_result.eval(), "\n")
        print("The result matrix has shape", multiply_result.get_shape())


def exercise_variables_init_assign():
    # Create a graph
    g = tf.Graph()

    with g.as_default(), tf.Session() as sess:
        # Create a variable with initial value 3
        v = tf.Variable([3])

        # Create a variable of shape [1], with initial random value,
        # sampled from a normal distribution with mean 1 and standard
        # deviation 0.35
        w = tf.Variable(tf.random_normal([1], mean=1.0, stddev=0.35))
        sess.run(tf.global_variables_initializer())
        print("The result of executing 'exercise_variables_init_assign' is:")
        print("Original v value:", v.eval())
        print("w value:", w.eval())
        assign_op = tf.assign(v, [7])
        print("After reassignment but run op not performed", v.eval())
        sess.run(assign_op)
        print("v value after reassignment:", v.eval())


def exercise2():
    # Create a graph
    g = tf.Graph()

    with g.as_default(), tf.Session() as sess:
        # Place dice throws inside two separate 10x1 matrices
        dice1 = tf.Variable(tf.random_uniform([10, 1], minval=1, maxval=7,
                                              dtype=tf.int32))
        dice2 = tf.Variable(tf.random_uniform([10, 1], minval=1, maxval=7,
                                              dtype=tf.int32))

        # Calculate the 3th row adding dice1 and dice2
        dice_sum = tf.add(dice1, dice2)

        # We've got three separate 10x1 matrices. To produce a single
        # 10x3 matrix, we'll concatenate them along dimension 1
        matrix = tf.concat(values=[dice1, dice2, dice_sum], axis=1)

        # Initialize variables
        sess.run(tf.global_variables_initializer())

        print("The result of executing 'exercise2' is:")
        print("The dice matrix simulation is\n", matrix.eval())


# simple_tensorflow_program()
# exercise_third_operand()
# exercise_vector_addition()
# exercise_tensor_shapes()
# exercise_broadcasting()
# exercise_matrix_multiplication()
exercise_tensor_reshaping()
exercise1()
exercise_variables_init_assign()
exercise2()
