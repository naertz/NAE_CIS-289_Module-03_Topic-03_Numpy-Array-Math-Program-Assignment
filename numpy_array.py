"""
Program:               numpy_array.py
Author:                Noah Allan Ertz
Last Date Modified:    2021-09-15

Prints values of numpy arrays
"""

import numpy as np

if __name__ == '__main__':
    first_np_array = np.array([[10, 15, 20], [2, 3, 4], [9, 14.5, 18]])
    second_np_array = np.array([[1, 2, 5], [8, 0, 12], [11, 3, 22]])

    print('First Numpy Array', end='\n\n')
    print('Original', end='\n\n')
    print(first_np_array, end='\n\n')
    print('Shape', end='\n\n')
    print(first_np_array.shape, end='\n\n')
    print('2x2 slice from [0, 0] to [1, 1]', end='\n\n')
    print(first_np_array[0:2, 0:2], end='\n\n')
    print('Is Even', end='\n\n')
    print(np.where(first_np_array % 2 > 0, False, True), end='\n\n')

    print('Add first and second numpy array', end='\n\n')
    print(np.add(first_np_array, second_np_array), end='\n\n')
    print('Multiply first and second numpy array', end='\n\n')
    print(np.multiply(first_np_array, second_np_array), end='\n\n')

    print('Second Numpy Array', end='\n\n')
    print('Sum', end='\n\n')
    print(np.sum(second_np_array), end='\n\n')
    print('Product', end='\n\n')
    print(np.product(second_np_array), end='\n\n')
    print('Max', end='\n\n')
    print(np.max(second_np_array), end='\n\n')
    print('Min', end='\n\n')
    print(np.min(second_np_array))
