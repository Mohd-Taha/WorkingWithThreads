from audioop import avg
from threading import Thread
import matplotlib.pyplot as plt
import time
import random

from numpy import average


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        # print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def createNumberFile(size):
    with open("D:\\Uni Kaam\\4th Year\\PC & DC\\codingTasks\\randomNumbers.txt", "w") as outputfile:
        for x in (random.randint(0, 100) for x in range(size)):
            outputfile.write(str(x))
            outputfile.write('\n')


def readData():
    with open("D:\\Uni Kaam\\4th Year\\PC & DC\\codingTasks\\randomNumbers.txt", "r") as inputFile:
        inputData = inputFile.read()
        inputData = inputData.split('\n')
        return inputData[:-1]


def chunks(lst, n):
    return [lst[i::n] for i in range(n)]


def calculateSum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum


def plotGraph(x, y, xLabel, yLabel, head):
    plt.plot(x, y)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(head)
    plt.show()
    return


if __name__ == "__main__":
    create = int(input("Create New Test List (0 for Yes):\t"))
    if (create == 0):
        size = int(input("Test List Size:\t\t\t"))
        createNumberFile(size)
    num = int(input("Number of Threads:\t\t\t"))
    if (num < 1):
        print("Threads Can't be Less Than 1. Testing for 1 Thread")
        num = 1
    numThreads = []
    maxTimes = []
    data = readData()
    data = list(map(float, data))
    data = list(map(int, data))
    dataSet = []
    for i in range(10):
        dataHere = data
        dataSet.append(dataHere)
    size = len(data)
    for i in range(num, 0, -1):
        threads = []
        startTimes = []
        timeTaken = []
        numThreads.append(i)
        dataLists = chunks(data, i)
        for j in range(i):
            x = dataLists[i-1]
            t = ThreadWithReturnValue(target=calculateSum, args=(x,))
            threads.append(t)
            startTimes.append(0)
            timeTaken.append(0)
        print("thread", i, threads)
        finalSum = 0
        for i, j in enumerate(threads):
            startTimes[i] = time.time()
            j.start()
        for i, j in enumerate(threads):
            x = j.join()
            finalSum += x
            timeTaken[i] = time.time() - startTimes[i]
        maxTimes.append(min(timeTaken))
        print(timeTaken)
        print(maxTimes[-1])
    print("\t*****See Line Chart*****")
    # print("timeTaken", timeMax)
    # print("numThreads", numThreads)
    plotGraph(numThreads, maxTimes, 'Number of Threads', 'Max Execution Time',
              'Time Optimization Test ( Test List Size: 1M , Returned Sum: ' + str(finalSum) + ' )')
