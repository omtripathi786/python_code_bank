import numpy as np
import time


def basic_demo():
    # time difference between normal python and numpy
    x = np.random.random(100000000)
    start = time.time()
    sum(x) / len(x)
    print(time.time() - start)
    start = time.time()
    np.mean(x)
    print(time.time() - start)


def print_array(nd_array):
    print('Element: ', nd_array)
    print('Shape: ', nd_array.shape)
    print('Size: ', nd_array.size)
    print('dtype: ', nd_array.dtype)
    print('---------------------')


def create_array():
    x = np.array([1, 2, 3, 4, 5])
    print_array(x)
    np.save('my_array', x)
    y = np.load('my_array.npy')
    print(y)


def generate_np_array():
    x = np.zeros((3, 4))
    print_array(x)
    y = np.ones((4, 3))
    print_array(y)
    z = np.eye(5)
    print_array(z)
    a = np.diag([9,8,7])
    print_array(a)
    #arange


if __name__ == '__main__':
    # basic_demo()
    create_array()
    generate_np_array()
