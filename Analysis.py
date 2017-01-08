__author__ = 'John'

import time
from timeit import *
import random


def minInList1(list_of_numbs):
    min = list_of_numbs[0]
    for i in range(len(list_of_numbs)):
        if i < min:
            min = i
    return min

def minInList2(list_of_numbs):
    for i in range(len(list_of_numbs)-1):
        for j in range(i+1, len(list_of_numbs)):
            if list_of_numbs[i] > list_of_numbs[j]:
                t = list_of_numbs[i]
                list_of_numbs[i] = list_of_numbs[j]
                list_of_numbs[j] = t
    return list_of_numbs[0]

mylist = []
n = 5
for i in range(1,n+1):
    mylist.append(random.randrange(100))

start = time.time()
minInList1(mylist)
print("Time 1: " + str(time.time()-start))

start = time.time()
minInList2(mylist)
print("Time 2: " + str(time.time()-start))



def anagramSolution4(s1,s2):
    c1 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c1[pos] = c1[pos] - 1

    for j in c1:
        if j != 0:
            return False

    return True


print(anagramSolution4('apples','spleap'))


def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")



