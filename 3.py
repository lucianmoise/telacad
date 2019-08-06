from functools import reduce
import multiprocessing
import time

start = time.perf_counter()

t = range(99999, 100003)

a = []
mp = []


def factorial(j):
    v = 1
    for z in range(1, j + 1):
        v = v * z
    return v


if __name__ == '__main__':

    pool_size = len(t)
    pool = multiprocessing.Pool(processes=pool_size)
    inputs = list(t)
    a = pool.map(factorial, inputs)
    pool.close()

    end = time.perf_counter()

    print("Factorial de numerele respective au fost generate in {}".format(end-start))


    start = time.perf_counter()

    # def writefile(filename):
    #     with open(filename) + ".txt", 'w') as file:
    #        file.write(str([1]))
    #
    #
    # for i in zip(t, a):
    #     p = multiprocessing.Process(target=factorial, args=(i,))
    #     mp.append(p)
    #     p.start()



    # end = time.perf_counter()

    print(len(a))

    print("Numerele factorial generate au fost scrise in fisiere in {}".format(end-start))