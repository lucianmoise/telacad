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
    a.append(v)  # nu-l adauga


if __name__ == '__main__':

    # pool_size = len(t)
    # pool = multiprocessing.Pool(processes=pool_size, initializer=factorial)
    # print(list(t))
    # inputs = list(t)
    # a = pool.map(factorial, inputs)
    # pool.close()

    for i in t:
        p = multiprocessing.Process(target=factorial, args=(i,))
        mp.append(p)
        p.start()
    [y.join() for y in mp]

    end = time.perf_counter()

    print("Factorial de numerele respective au fost generate in {}".format(end-start))

    start = time.perf_counter()

    for i in zip(t, a):

       with open(str(i[0]) + ".txt", 'w') as file:

           file.write(str(i[1]))

    end = time.perf_counter()

    print(len(a))

    print("Numerele factorial generate au fost scrise in fisiere in {}".format(end-start))