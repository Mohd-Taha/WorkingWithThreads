    # size = len(data)
    # for i in range(num, 0,-1):
    #     timeTaken = []
    #     threads = []
    #     numThreads.append(i)
    #     dataLists = chunks(data, i)
    #     for j in range(i):
    #         x = dataLists[i-1]
    #         t = threading.Thread(target=calculateSum, args=(x,))
    #         threads.append(t)
    #     print("thread", i, threads)
    #     finalSum = 0
    #     for j in threads:
    #         startTime = time.time()
    #         j.start()
    #     for j in threads:
    #         x = j.join()
    #         timeTaken.append(time.time() - startTime)
    #     timeMax.append(max(timeTaken))
    # # print("timeTaken", timeMax)
    # # print("numThreads", numThreads)
    # plotGraph(numThreads, timeMax, 'Number of Threads', 'Max Execution Time',
    #           'Time Optimization Test ( Testing list size: '+ str(size) +' )')
