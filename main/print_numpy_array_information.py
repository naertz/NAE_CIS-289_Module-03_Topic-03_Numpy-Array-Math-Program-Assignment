"""
Program:               print_numpy_array_information.py
Author:                Noah Allan Ertz
Last Date Modified:    2021-09-18

Prints information of two numpy arrays.
"""

from numpy import add, max, min, multiply, product, sum, where

from numpy_arrays import TITLE_FIRST_NUMPY_ARRAY, TITLE_SECOND_NUMPY_ARRAY, TITLE_FIRST_AND_SECOND_NUMPY_ARRAYS, FIRST_NUMPY_ARRAY, SECOND_NUMPY_ARRAY


def print_numpy_array(title, numpy_array):
    """
    Prints title and original numpy array.

    :param title: title for numpy array
    :param numpy_array: numpy array
    :return: N/A
    """
    print(f'{title}:', end='\n\n')
    print('Original Numpy Array:', end='\n\n')
    print(numpy_array)


def print_numpy_array_shape(numpy_array):
    """
    Prints numpy array shape.

    :param numpy_array: numpy array
    :return: N/A
    """
    print('Numpy Array Shape:', end='\n\n')
    print(numpy_array.shape)


def print_top_left_two_by_two_slice(numpy_array):
    """
    Prints top left two by two slice of numpy array.

    :param numpy_array: numpy array
    :return: N/A
    """
    print('2x2 Slice From [0, 0] To [1, 1]:', end='\n\n')
    print(numpy_array[0:2, 0:2])


def print_numpy_array_elements_replaced_with_is_even_boolean_result(numpy_array):
    """
    Replaces numpy array elements with booleans where an element is true if it is even and prints the numpy array.

    :param numpy_array: numpy array
    :return: N/A
    """
    print('Is Even:', end='\n\n')
    print(where(numpy_array % 2 > 0, False, True))


def print_sum_of_numpy_array_elements(numpy_array):
    """
    Prints sum of numpy array elements.

    :param numpy_array: numpy array
    :return: N/A
    """
    print(f'Sum: {str(sum(numpy_array))}')


def print_product_of_numpy_array_elements(numpy_array):
    """
    Prints product of numpy array elements.

    :param numpy_array: numpy array
    :return: N/A
    """
    print(f'Product: {str(product(numpy_array))}')


def print_minimum_and_maximum_elements_of_numpy_array(numpy_array):
    """
    Prints minimum and maximum elements of numpy array.

    :param numpy_array: numpy array
    :return: N/A
    """
    print(f'Min: {str(min(numpy_array))}')
    print(f'Max: {str(max(numpy_array))}')


def print_numpy_arrays(title, first_numpy_array, second_numpy_array):
    """
    Prints title and original numpy arrays.

    :param title: title for numpy arrays
    :param first_numpy_array: first numpy array
    :param second_numpy_array: second numpy array
    :return: N/A
    """
    print(f'{title}:', end='\n\n')
    print(f'{TITLE_FIRST_NUMPY_ARRAY}:', end='\n\n')
    print(first_numpy_array, end='\n\n')
    print(f'{TITLE_SECOND_NUMPY_ARRAY}:', end='\n\n')
    print(second_numpy_array)


def print_added_numpy_arrays(first_numpy_array, second_numpy_array):
    """
    Prints numpy array calculated from added first and second numpy arrays.

    :param first_numpy_array: first numpy array
    :param second_numpy_array: second numpy array
    :return: N/A
    """
    print('Added numpy arrays:', end='\n\n')
    print(add(first_numpy_array, second_numpy_array))


def print_multiplied_numpy_arrays(first_numpy_array, second_numpy_array):
    """
    Prints numpy array calculated from multiplied first and second numpy arrays.

    :param first_numpy_array: first numpy array
    :param second_numpy_array: second numpy array
    :return: N/A
    """
    print('Multiplied numpy arrays:', end='\n\n')
    print(multiply(first_numpy_array, second_numpy_array))


def print_first_numpy_array_information(title_numpy_array=TITLE_FIRST_NUMPY_ARRAY, numpy_array=FIRST_NUMPY_ARRAY):
    """
    Prints first numpy array information.

    :param title_numpy_array: title for numpy array
    :param numpy_array: numpy array
    :return: N/A
    """
    print_numpy_array(title_numpy_array, numpy_array)
    print()
    print_numpy_array_shape(numpy_array)
    print()
    print_top_left_two_by_two_slice(numpy_array)
    print()
    print_numpy_array_elements_replaced_with_is_even_boolean_result(numpy_array)


def print_second_numpy_array_information(title_numpy_array=TITLE_SECOND_NUMPY_ARRAY, numpy_array=SECOND_NUMPY_ARRAY):
    """
    Prints second numpy array information.

    :param title_numpy_array: title for numpy array
    :param numpy_array: numpy array
    :return: N/A
    """
    print_numpy_array(title_numpy_array, numpy_array)
    print()
    print_sum_of_numpy_array_elements(numpy_array)
    print_product_of_numpy_array_elements(numpy_array)
    print_minimum_and_maximum_elements_of_numpy_array(numpy_array)


def print_first_and_second_numpy_array_information(title_numpy_arrays=TITLE_FIRST_AND_SECOND_NUMPY_ARRAYS, first_numpy_array=FIRST_NUMPY_ARRAY, second_numpy_array=SECOND_NUMPY_ARRAY):
    """
    Prints first and second numpy array information.

    :param title_numpy_arrays: title for numpy arrays
    :param first_numpy_array: first numpy array
    :param second_numpy_array: second numpy array
    :return: N/A
    """
    print_numpy_arrays(title_numpy_arrays, first_numpy_array, second_numpy_array)
    print()
    print_added_numpy_arrays(first_numpy_array, second_numpy_array)
    print()
    print_multiplied_numpy_arrays(first_numpy_array, second_numpy_array)


if __name__ == '__main__':
    print_first_numpy_array_information()
    print('\n')
    print_second_numpy_array_information()
    print('\n')
    print_first_and_second_numpy_array_information()
