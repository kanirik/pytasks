import sys
from bitarray import bitarray
import time

def calc(n):
    ln = n - 1
    maxnum = n + 1
    lst = bitarray(ln)
    lst.setall(True)
    unity = bitarray(1)
    unity.setall(True)
    p = 0
    while 2 * p + 4 <= maxnum:
        lst[2 * p + 2: n : p + 2] = False
        pos = lst[p + 1:n].search(unity, 1)
        if len(pos) == 0:
            break
        else:
            p += pos[0] + 1
    return lst

def arrayToList(array):
    return [i + 2 for i, el in enumerate(array) if el]

if __name__ == '__main__':
    time0 = time.time()
    array = calc(int(sys.argv[1]))
    time1 = time.time()
    print 'time: ', time1 - time0
    #print arrayToList(array)
